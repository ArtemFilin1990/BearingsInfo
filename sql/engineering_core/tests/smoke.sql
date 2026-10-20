\set ON_ERROR_STOP on
DO $$ BEGIN
 IF current_database() <> 'everest_bearings_ci' THEN
  RAISE EXCEPTION 'Refusing smoke test outside isolated everest_bearings_ci database';
 END IF;
 IF (SELECT count(*) FROM information_schema.tables WHERE table_schema='everest_engineering')<>10 THEN
  RAISE EXCEPTION 'Missing required engineering tables';
 END IF;
END $$;
BEGIN;
INSERT INTO everest_engineering.source_documents(id,document_type,publisher,title,source_version)
 VALUES('test-doc','OTHER','Test suite','Non-production fixture','1');
INSERT INTO everest_engineering.bearing_products
 (id,original_raw_designation,brand,standard_system,basic_designation,attribute_profile,origin_document_id)
 VALUES ('test-a','6205','SKF','ISO','6205','RADIAL_BALL_V1','test-doc'),
        ('test-b','6305','SKF','ISO','6305','RADIAL_BALL_V1','test-doc');
INSERT INTO everest_engineering.bearing_equivalences
 (id,source_bearing_id,candidate_bearing_id,discovery_source_id,candidate_basis)
 VALUES ('test-pair','test-a','test-b','test-doc','DIMENSIONS');
INSERT INTO everest_engineering.attribute_provenance
 (bearing_id,attribute_name,origin,canonical_value)
 VALUES ('test-a','clearance','UNKNOWN',NULL);
DO $$ BEGIN
 BEGIN
  INSERT INTO everest_engineering.attribute_provenance
   (bearing_id,attribute_name,origin,canonical_value)
   VALUES('test-a','precision','EXPLICIT','NORMAL');
  RAISE EXCEPTION 'invalid explicit evidence was accepted';
 EXCEPTION WHEN check_violation THEN NULL;
 END;
 BEGIN
  INSERT INTO everest_engineering.analogue_decisions
   (id,equivalence_id,status,approved_by,approval_date,valid_until,justification,
    restrictions,evidence_source_id,source_snapshot_digest,candidate_snapshot_digest)
   VALUES('unsafe','test-pair','CONDITIONAL','engineer',date '2026-10-21',date '2027-01-01',
    'unscoped','["limit"]','test-doc',repeat('a',64),repeat('b',64));
  RAISE EXCEPTION 'unscoped conditional was accepted';
 EXCEPTION WHEN check_violation THEN NULL;
 END;
END $$;
INSERT INTO everest_engineering.analogue_decisions(id,equivalence_id,status)
 VALUES('dimensional-only','test-pair','DIMENSIONAL');
INSERT INTO everest_engineering.decision_audit
 (decision_id,operation,actor,allowed,reason_codes)
 VALUES('dimensional-only','DENIED','smoke-suite',FALSE,'["NO_APPROVED_DECISION"]');
DO $$ BEGIN
 BEGIN
  UPDATE everest_engineering.decision_audit SET allowed=TRUE WHERE actor='smoke-suite';
 EXCEPTION WHEN raise_exception THEN NULL;
 END;
 IF (SELECT allowed FROM everest_engineering.decision_audit WHERE actor='smoke-suite') THEN
  RAISE EXCEPTION 'append-only audit was modified';
 END IF;
END $$;
ROLLBACK;
SELECT 'engineering-core smoke passed' AS result;
