"""Regression tests for the isolated 74-brand normalization staging pipeline."""
import csv
import sqlite3
import tempfile
import unittest
from pathlib import Path
from normalize_snapshot import split_designation, build

class TypeFirstTests(unittest.TestCase):
    def test_type_first(self):
        examples = {
            "ШС12": ("","ШС12","","SPHERICAL_PLAIN"),
            "2ШС 20": ("","2ШС20","","SPHERICAL_PLAIN"),
            "ШСЛ90К1": ("","ШСЛ90","К1","SPHERICAL_PLAIN"),
            "6-180205": ("6","180205","","UNKNOWN"),
            "(70)32134Л": ("70","32134","Л","UNKNOWN"),
            "(70) 32134Л": ("70","32134","Л","UNKNOWN"),
            "(70)-32134Л": ("70","32134","Л","UNKNOWN"),
            "NU 205 ECP/C3": ("","NU205","ECP/C3","CYLINDRICAL_ROLLER"),
            "HK1616": ("","HK1616","","NEEDLE"),
            "UCP205": ("","UCP205","","MOUNTED_UNIT_OR_INSERT"),
            "7205": ("","7205","","UNKNOWN"),
        }
        for designation, expected in examples.items():
            with self.subTest(designation=designation):
                self.assertEqual(split_designation(designation)[:4],expected)

    def test_parenthesized_numeric_prefix_is_safe_but_assembly_is_not(self):
        prefix, body, suffix, _, _, status, issues = split_designation("(70)32134Л")
        self.assertEqual(f"{prefix}-{body}{suffix}", "70-32134Л")
        self.assertEqual((status, issues), ("PARSED", []))

        *_, status, issues = split_designation("(70)32134Л (комплект)")
        self.assertEqual(status, "REVIEW")
        self.assertIn("ASSEMBLY_OR_PARENTHESIS", issues)

    def test_all_74_brands_staged_only(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root/"source.csv"
            with source.open("w",encoding="utf-8",newline="") as handle:
                writer=csv.writer(handle)
                writer.writerow(["Brand","Product Name","Product Link","Analog Name","Analog Link","Factory"])
                for i in range(74):
                    writer.writerow([f"BRAND{i}","ШС12" if i%2 else "NU 205 ECP/C3","","6205","",""])
            output, report = root/"snapshot.sqlite",root/"report.json"
            result=build(source,output,report,min_rows=74,min_brands=74)
            self.assertEqual((result["rows"],result["brands"]),(74,74))
            self.assertEqual(result["bearing_type_hint_counts"],
                             {"CYLINDRICAL_ROLLER":37,"SPHERICAL_PLAIN":37})
            self.assertEqual(result["unknown_type_hint_rows"],0)
            db=sqlite3.connect(output)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM stage_designations WHERE semantic_status='UNVERIFIED'").fetchone()[0],74)
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchone()[0],"ok")
            db.close()

if __name__=="__main__":
    unittest.main()
