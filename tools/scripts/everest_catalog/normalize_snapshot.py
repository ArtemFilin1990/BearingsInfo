#!/usr/bin/env python3
"""EVEREST type-first read-only staging of the full aggregated nomenclature."""
import argparse
import csv
import hashlib
import json
import re
import sqlite3
import unicodedata
from collections import Counter
from pathlib import Path

RULESET = "EVEREST-TYPE-FIRST-3.0"
EXPECTED_HEADER = ["Brand","Product Name","Product Link","Analog Name","Analog Link","Factory"]
JOINT = re.compile(r"^(?:[0-9]|G|Е)?(ШСЛ|ШСП|ШС|Ш)\s*(\d{1,5})(.*)$")
SERIES = ("UCFL","UCFC","UCPA","UCPH","UCFB","UCP","UCT","UCF","UC","UK",
          "RNAO","RNA","NKI","NKIS","NKS","NK","NAO","NA","AXK","HK","BK",
          "NUP","NU","NJ","NF","QJ","N","LME","LMB","LMK","LM")

def split_designation(original):
    value = unicodedata.normalize("NFKC",original or "").upper().strip()
    value = re.sub(r"\s+"," ",value.translate(str.maketrans("–—−‑","----")))
    issues = []
    if not value:
        return "","","","UNKNOWN","","INVALID",["EMPTY"]
    if value.startswith('"') or value.endswith('"'):
        issues.append("QUOTED")
        value = value.strip('"')
    if re.search("[A-Z]",value) and re.search("[А-ЯЁ]",value):
        issues.append("MIXED_ALPHABETS")
    prefix = ""
    # A leading numeric value in parentheses is a prefix, not part of the
    # bearing body: (70)32134Л -> 70-32134Л.  Other parentheses still need
    # manual review because they may describe assemblies or options.
    match = re.fullmatch(r"\((\d{1,4})\)\s*-?\s*(.+)", value)
    if match:
        prefix, value = match.groups()
    else:
        match = re.fullmatch(r"(\d[\dА-ЯЁA-Z]{0,3})-(.+)", value)
        if match:
            prefix, value = match.groups()
    if re.search(r"[+()\[\]]",value):
        issues.append("ASSEMBLY_OR_PARENTHESIS")
    match=JOINT.fullmatch(value)
    if match:
        body=value[:match.end(2)].replace(" ","")
        suffix=match.group(3).strip()
        kind,family="SPHERICAL_PLAIN",match.group(1)
    else:
        matched=False
        for series in sorted(SERIES,key=len,reverse=True):
            m=re.fullmatch(re.escape(series)+r"\s*(\d{1,9})(.*)",value)
            if not m:
                continue
            body,suffix,family=series+m.group(1),m.group(2).strip(),series
            kind=("MOUNTED_UNIT_OR_INSERT" if series.startswith(("UC","UK"))
                  else "NEEDLE" if series in {"RNAO","RNA","NKI","NKIS","NKS","NK","NAO","NA","AXK","HK","BK"}
                  else "CYLINDRICAL_ROLLER" if series in {"NUP","NU","NJ","NF","N"}
                  else "LINEAR_BALL" if series in {"LME","LMB","LMK","LM"}
                  else "FOUR_POINT_CONTACT_BALL" if series=="QJ" else "UNKNOWN")
            matched=True
            break
        if not matched:
            m=re.fullmatch(r"(\d{1,9}(?:/\d{1,7})?)(.*)",value)
            if m:
                body,suffix,family,kind=m.group(1),m.group(2).strip(),"","UNKNOWN"
            else:
                body,suffix,family,kind=value,"","","UNKNOWN"
                issues.append("NO_SAFE_FAMILY_RULE")
    return prefix,body,suffix,kind,family,("REVIEW" if issues else "PARSED"),sorted(set(issues))

def build(source,output,report,min_rows=40000,min_brands=74):
    data=source.read_bytes()
    blob=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    report.parent.mkdir(parents=True,exist_ok=True)
    tmp=output.with_suffix(output.suffix+".partial")
    tmp.unlink(missing_ok=True)
    db=sqlite3.connect(tmp)
    try:
        db.executescript("""
        CREATE TABLE stage_designations (
          source_line INTEGER PRIMARY KEY, brand TEXT NOT NULL, original_designation TEXT NOT NULL,
          prefix TEXT NOT NULL, body TEXT NOT NULL, suffix TEXT NOT NULL, bearing_type_hint TEXT NOT NULL,
          family TEXT NOT NULL, parse_status TEXT NOT NULL, issues_json TEXT NOT NULL,
          semantic_status TEXT NOT NULL CHECK(semantic_status='UNVERIFIED'),
          analogue_raw TEXT, product_link_raw TEXT, analogue_link_raw TEXT, factory_raw TEXT,
          origin_file TEXT NOT NULL, origin_blob_sha TEXT NOT NULL, ruleset TEXT NOT NULL
        );
        CREATE INDEX stage_brand_body ON stage_designations(brand,body);
        """)
        brands=Counter()
        statuses=Counter()
        type_hints=Counter()
        unique=set()
        with source.open(encoding="utf-8-sig",newline="") as stream:
            reader=csv.DictReader(stream)
            if reader.fieldnames!=EXPECTED_HEADER:
                raise ValueError(f"Unexpected columns {reader.fieldnames}")
            for row in reader:
                brand=(row["Brand"] or "").strip()
                raw=(row["Product Name"] or "").strip()
                if not brand or not raw:
                    raise ValueError(f"Blank brand/designation at source line {reader.line_num}")
                prefix,body,suffix,kind,family,status,issues=split_designation(raw)
                db.execute("""INSERT INTO stage_designations VALUES
                  (?,?,?,?,?,?,?,?,?,?,'UNVERIFIED',?,?,?,?,?,?,?)""",(
                  reader.line_num,brand,raw,prefix,body,suffix,kind,family,status,
                  json.dumps(issues,ensure_ascii=False),row["Analog Name"],row["Product Link"],
                  row["Analog Link"],row["Factory"],"data/nomenclature.csv",blob,RULESET))
                brands[brand]+=1
                statuses[status]+=1
                type_hints[kind]+=1
                unique.add((brand,raw))
        rows=sum(brands.values())
        if rows<min_rows or len(brands)<min_brands:
            raise ValueError(f"Incomplete input: rows={rows}, brands={len(brands)}")
        db.commit()
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":
            raise RuntimeError("SQLite integrity check failed")
        assert db.execute("SELECT COUNT(*) FROM stage_designations WHERE semantic_status!='UNVERIFIED'").fetchone()[0]==0
        result={"rows":rows,"brands":len(brands),"unique_brand_designations":len(unique),
                "duplicate_source_rows":rows-len(unique),"parse_status_counts":dict(statuses),
                "bearing_type_hint_counts":dict(sorted(type_hints.items())),
                "unknown_type_hint_rows":type_hints["UNKNOWN"],
                "brand_row_counts":dict(sorted(brands.items())),"source_blob_sha":blob,
                "ruleset":RULESET,"semantic_status":"ALL_UNVERIFIED",
                "production_database_changed":False}
        db.close()
        tmp.replace(output)
        report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        return result
    except BaseException:
        db.close()
        tmp.unlink(missing_ok=True)
        raise

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,default=Path("data/nomenclature.csv"))
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--min-rows",type=int,default=40000)
    p.add_argument("--min-brands",type=int,default=74)
    args=p.parse_args()
    result=build(args.input,args.output,args.report,args.min_rows,args.min_brands)
    print(json.dumps({k:v for k,v in result.items() if k!="brand_row_counts"},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
