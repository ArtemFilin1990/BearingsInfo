\set ON_ERROR_STOP on
-- Run only against a disposable PostgreSQL database.
DO $$ BEGIN
  IF current_database() <> 'everest_bearings_ci' THEN
    RAISE EXCEPTION 'Refusing smoke outside everest_bearings_ci';
  END IF;
END $$;

BEGIN;
DO $$ DECLARE n integer; BEGIN
  SELECT count(*) INTO n FROM information_schema.tables WHERE table_schema = 'everest_engineering';
  IF n <> 10 THEN RAISE EXCEPTION 'Expected ten engineering tables, found %', n; END IF;
  IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='everest_engineering' AND column_name='is_direct_analog') THEN
    RAISE EXCEPTION 'Legacy unsafe is_direct_analog field leaked to engineering schema';
  END IF;
END $$;

INSERT INTO everest_engineering.source_documents(id,document_type,publisher,title,source_version)
 VALUES('smoke-doc','OTHER','Test suite','Ephemeral verification','1');
INSERT INTO everest_engineering.bearing_products
 (id,original_raw_designation,brand,standard_system,basic_designation,attribute_profile,origin_document_id)
 VALUES ('smoke-a','6205','SKF','ISO','6205','RADIAL_BALL_V1','smoke-doc'),
        ('smoke-b','6305','SKF','ISO','6305','RADIAL_BALL_V1','smoke-doc');
INSERT INTO everest_engineering.bearing_equivalences
 (id,source_bearing_id,candidate_bearing_id,discovery_source_id,candidate_basis)
 VALUES ('smoke-pair','smoke-a','smoke-b','smoke-doc','DIMENSIONS');
INSERT INTO everest_engineering.attribute_provenance
 (bearing_id,attribute_name,origin,canonical_value)
 VALUES ('smoke-a','clearance','UNKNOWN',NULL);

-- Expected-failure tests must assert a CHECK error actually occurred.
DO $$ DECLARE rejected boolean := FALSE; BEGIN
  BEGIN
    INSERT INTO everest_engineering.attribute_provenance
      (bearing_id,attribute_name,origin,canonical_value)
      VALUES ('smoke-a','precision','EXPLICIT','NORMAL');
  EXCEPTION WHEN check_violation THEN rejected := TRUE;
  END;
  IF NOT rejected THEN RAISE EXCEPTION 'BUG: Explicit provenance without source was accepted'; END IF;
END $$;
DO $$ DECLARE rejected boolean := FALSE; BEGIN
  BEGIN
    INSERT INTO everest_engineering.analogue_decisions
      (id,equivalence_id,status,approved_by,approval_date,valid_until,justification,
       restrictions,evidence_source_id,source_snapshot_digest,candidate_snapshot_digest)
      VALUES ('smoke-unsafe','smoke-pair','CONDITIONAL','engineer',date '2026-10-21',
       date '2027-01-01','unscoped','["limit"]'::jsonb,'smoke-doc',repeat('a',64),repeat('b',64));
  EXCEPTION WHEN check_violation THEN rejected := TRUE;
  END;
  IF NOT rejected THEN RAISE EXCEPTION 'BUG: CONDITIONAL without scope was accepted'; END IF;
END $$;

INSERT INTO everest_engineering.analogue_decisions(id,equivalence_id,status)
 VALUES ('smoke-dimensional','smoke-pair','DIMENSIONAL');
INSERT INTO everest_engineering.decision_audit(decision_id,operation,actor,allowed,reason_codes)
 VALUES ('smoke-dimensional','DENIED','smoke-suite',FALSE,'["NO_APPROVED_DECISION"]'::jsonb);
DO $$ DECLARE rejected boolean := FALSE; msg text; BEGIN
  BEGIN
    UPDATE everest_engineering.decision_audit SET allowed=TRUE WHERE actor='smoke-suite';
  EXCEPTION WHEN raise_exception THEN
    GET STACKED DIAGNOSTICS msg = MESSAGE_TEXT;
    IF msg NOT LIKE 'Append-only%' THEN RAISE; END IF;
    rejected := TRUE;
  END;
  IF NOT rejected THEN RAISE EXCEPTION 'BUG: audit UPDATE was accepted'; END IF;
  IF (SELECT allowed FROM everest_engineering.decision_audit WHERE actor='smoke-suite') THEN
     RAISE EXCEPTION 'BUG: audit row was modified'; END IF;
END $$;
DO $$ DECLARE rejected boolean := FALSE; msg text; BEGIN
  BEGIN
    DELETE FROM everest_engineering.analogue_decisions WHERE id='smoke-dimensional';
  EXCEPTION WHEN raise_exception THEN
    GET STACKED DIAGNOSTICS msg = MESSAGE_TEXT;
    IF msg NOT LIKE 'Append-only%' THEN RAISE; END IF;
    rejected := TRUE;
  END;
  IF NOT rejected THEN RAISE EXCEPTION 'BUG: decision DELETE was accepted'; END IF;
END $$;
ROLLBACK;
SELECT 'PASS: temporary PostgreSQL 16 engineering migration + fail-closed checks' AS result;
