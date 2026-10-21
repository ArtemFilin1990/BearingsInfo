-- EVEREST BearingsInfo engineering_core schema v1 — PostgreSQL 14+
-- Isolated: DOES NOT ALTER legacy public.bearings, public.analogs or old find_analogs().
-- No inserts, no guessed equivalences, no default confirmed status.
BEGIN;
CREATE SCHEMA IF NOT EXISTS everest_engineering;

CREATE TABLE IF NOT EXISTS everest_engineering.source_documents (
    id TEXT PRIMARY KEY,
    document_type TEXT NOT NULL CHECK (document_type IN ('STANDARD','OEM_CATALOG','DRAWING','INVOICE','ENGINEERING_REPORT','OTHER')),
    publisher TEXT NOT NULL,
    title TEXT NOT NULL,
    source_url TEXT,
    source_version TEXT NOT NULL,
    publication_date DATE,
    sha256 CHAR(64),
    registered_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS everest_engineering.standard_editions (
    id TEXT PRIMARY KEY,
    standards_body TEXT NOT NULL CHECK (standards_body IN ('GOST','GOST_R','ISO','DIN','OTHER')),
    standard_number TEXT NOT NULL,
    edition_year INTEGER NOT NULL CHECK (edition_year BETWEEN 1900 AND 2200),
    full_designation TEXT NOT NULL,
    lifecycle_status TEXT NOT NULL CHECK (lifecycle_status IN ('ACTIVE','REPLACED','PROJECT','WITHDRAWN')),
    effective_date DATE,
    lifecycle_checked_at DATE NOT NULL,
    lifecycle_source_id TEXT NOT NULL REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    UNIQUE (standards_body, standard_number, edition_year)
);

CREATE TABLE IF NOT EXISTS everest_engineering.standards_crosswalk (
    id TEXT PRIMARY KEY,
    source_standard_edition_id TEXT NOT NULL REFERENCES everest_engineering.standard_editions(id) ON DELETE RESTRICT,
    target_standard_edition_id TEXT NOT NULL REFERENCES everest_engineering.standard_editions(id) ON DELETE RESTRICT,
    alignment TEXT NOT NULL CHECK (alignment IN ('IDT','MOD','NEQ')),
    differences TEXT,
    evidence_source_id TEXT NOT NULL REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    verified_at DATE NOT NULL,
    CHECK (source_standard_edition_id <> target_standard_edition_id),
    UNIQUE (source_standard_edition_id, target_standard_edition_id)
);
COMMENT ON TABLE everest_engineering.standards_crosswalk IS 'IDT/MOD/NEQ applies to standard editions, never to product substitution.';

CREATE TABLE IF NOT EXISTS everest_engineering.designation_dictionary (
    id TEXT PRIMARY KEY,
    brand TEXT NOT NULL, -- exact brand or explicitly documented GLOBAL standard grammar
    component TEXT NOT NULL CHECK (component IN ('PREFIX','BASIC_SERIES','SUFFIX')),
    code TEXT NOT NULL,
    semantic_feature TEXT NOT NULL,
    technical_meaning TEXT NOT NULL,
    bearing_scope TEXT NOT NULL,
    source_document_id TEXT NOT NULL REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    standard_edition_id TEXT REFERENCES everest_engineering.standard_editions(id) ON DELETE RESTRICT,
    active_from DATE,
    active_to DATE,
    CHECK (length(trim(code)) > 0),
    CHECK (active_to IS NULL OR active_from IS NULL OR active_to >= active_from),
    UNIQUE (brand, component, code, bearing_scope, source_document_id)
);

CREATE TABLE IF NOT EXISTS everest_engineering.bearing_products (
    id TEXT PRIMARY KEY,
    original_raw_designation TEXT NOT NULL,
    brand TEXT,
    standard_system TEXT NOT NULL,
    prefix TEXT NOT NULL DEFAULT '',
    basic_designation TEXT NOT NULL,
    suffix TEXT NOT NULL DEFAULT '',
    attribute_profile TEXT NOT NULL,
    origin_document_id TEXT NOT NULL REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (length(trim(basic_designation)) > 0)
);
CREATE INDEX IF NOT EXISTS idx_bearing_lookup
    ON everest_engineering.bearing_products(brand, basic_designation);

CREATE TABLE IF NOT EXISTS everest_engineering.attribute_provenance (
    id BIGSERIAL PRIMARY KEY,
    bearing_id TEXT NOT NULL REFERENCES everest_engineering.bearing_products(id) ON DELETE RESTRICT,
    attribute_name TEXT NOT NULL,
    canonical_value TEXT, -- dimension values must be canonical decimal mm; precision tolerance profiles are distinct
    original_value TEXT,
    unit TEXT,
    origin TEXT NOT NULL CHECK (origin IN ('EXPLICIT','STANDARD_DEFAULT','CATALOG_VERIFIED','UNKNOWN','CONFLICT')),
    source_document_id TEXT REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    source_version TEXT,
    standard_edition_id TEXT REFERENCES everest_engineering.standard_editions(id) ON DELETE RESTRICT,
    confidence NUMERIC(4,3) CHECK (confidence BETWEEN 0 AND 1),
    conflict_details TEXT,
    is_current BOOLEAN NOT NULL DEFAULT TRUE,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (
        (origin IN ('UNKNOWN','CONFLICT')) OR
        (canonical_value IS NOT NULL AND source_document_id IS NOT NULL AND source_version IS NOT NULL)
    ),
    CHECK (origin <> 'STANDARD_DEFAULT' OR (standard_edition_id IS NOT NULL AND confidence IS NOT NULL)),
    CHECK (origin <> 'CONFLICT' OR conflict_details IS NOT NULL),
    CHECK (origin <> 'UNKNOWN' OR canonical_value IS NULL)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_current_attribute_per_bearing
    ON everest_engineering.attribute_provenance(bearing_id, attribute_name) WHERE is_current;

CREATE TABLE IF NOT EXISTS everest_engineering.bearing_equivalences (
    id TEXT PRIMARY KEY,
    source_bearing_id TEXT NOT NULL REFERENCES everest_engineering.bearing_products(id) ON DELETE RESTRICT,
    candidate_bearing_id TEXT NOT NULL REFERENCES everest_engineering.bearing_products(id) ON DELETE RESTRICT,
    discovery_source_id TEXT NOT NULL REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    candidate_basis TEXT NOT NULL CHECK (candidate_basis IN ('DIRECT_CATALOG_REFERENCE','BASE_DESIGNATION','DIMENSIONS','SUPPLIER_CLAIM','OTHER')),
    observed_differences JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(observed_differences) = 'array'),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (source_bearing_id <> candidate_bearing_id),
    UNIQUE (source_bearing_id, candidate_bearing_id)
);
COMMENT ON TABLE everest_engineering.bearing_equivalences IS 'Directed candidate link, not a determination of interchangeability.';

CREATE TABLE IF NOT EXISTS everest_engineering.application_scopes (
    id TEXT PRIMARY KEY,
    site TEXT NOT NULL,
    equipment_id TEXT NOT NULL,
    bearing_position TEXT NOT NULL,
    operating_conditions_revision TEXT NOT NULL,
    description TEXT NOT NULL,
    UNIQUE (site, equipment_id, bearing_position, operating_conditions_revision)
);

CREATE TABLE IF NOT EXISTS everest_engineering.analogue_decisions (
    id TEXT PRIMARY KEY,
    equivalence_id TEXT NOT NULL REFERENCES everest_engineering.bearing_equivalences(id) ON DELETE RESTRICT,
    status TEXT NOT NULL CHECK (status IN ('CONFIRMED','BASIC','DIMENSIONAL','CONDITIONAL','REJECTED')),
    scope_id TEXT REFERENCES everest_engineering.application_scopes(id) ON DELETE RESTRICT,
    approved_by TEXT,
    approval_date DATE,
    valid_until DATE,
    justification TEXT,
    restrictions JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(restrictions) = 'array'),
    approved_differences JSONB NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(approved_differences) = 'array'),
    evidence_source_id TEXT REFERENCES everest_engineering.source_documents(id) ON DELETE RESTRICT,
    source_snapshot_digest CHAR(64),
    candidate_snapshot_digest CHAR(64),
    supersedes_decision_id TEXT UNIQUE REFERENCES everest_engineering.analogue_decisions(id) ON DELETE RESTRICT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (supersedes_decision_id IS NULL OR supersedes_decision_id <> id),
    CHECK (valid_until IS NULL OR approval_date IS NULL OR valid_until >= approval_date),
    CHECK (
        status NOT IN ('CONFIRMED','CONDITIONAL') OR
        (approved_by IS NOT NULL AND approval_date IS NOT NULL AND valid_until IS NOT NULL
        AND evidence_source_id IS NOT NULL AND justification IS NOT NULL
        AND source_snapshot_digest IS NOT NULL AND candidate_snapshot_digest IS NOT NULL)
    ),
    CHECK (status <> 'CONDITIONAL' OR (scope_id IS NOT NULL AND restrictions <> '[]'::jsonb)),
    CHECK (status <> 'CONFIRMED' OR approved_differences = '[]'::jsonb)
);
CREATE INDEX IF NOT EXISTS idx_analogue_decisions_context
    ON everest_engineering.analogue_decisions(equivalence_id, scope_id, approval_date);

CREATE TABLE IF NOT EXISTS everest_engineering.decision_audit (
    id BIGSERIAL PRIMARY KEY,
    decision_id TEXT REFERENCES everest_engineering.analogue_decisions(id) ON DELETE RESTRICT,
    operation TEXT NOT NULL CHECK (operation IN ('CREATED','EVALUATED','DENIED','SUPERSEDED','REVOKED')),
    actor TEXT NOT NULL,
    application_scope_id TEXT REFERENCES everest_engineering.application_scopes(id) ON DELETE RESTRICT,
    evaluated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    allowed BOOLEAN NOT NULL DEFAULT FALSE,
    reason_codes JSONB NOT NULL CHECK (jsonb_typeof(reason_codes) = 'array'),
    evidence_snapshot_hash CHAR(64)
);

CREATE OR REPLACE FUNCTION everest_engineering.reject_immutable_changes() RETURNS TRIGGER
LANGUAGE plpgsql AS $$ BEGIN RAISE EXCEPTION 'Append-only evidence/decision/audit; insert a superseding record'; END; $$;
CREATE TRIGGER forbid_decision_mutation BEFORE UPDATE OR DELETE ON everest_engineering.analogue_decisions
    FOR EACH ROW EXECUTE FUNCTION everest_engineering.reject_immutable_changes();
CREATE TRIGGER forbid_audit_mutation BEFORE UPDATE OR DELETE ON everest_engineering.decision_audit
    FOR EACH ROW EXECUTE FUNCTION everest_engineering.reject_immutable_changes();

-- Integration rule: never use legacy public.find_analogs() as a source of positive approval.
-- The application must verify immutable decision chain, active scope, evidence snapshots,
-- all critical attributes and authorization before writing an EVALUATED audit event.
COMMIT;
