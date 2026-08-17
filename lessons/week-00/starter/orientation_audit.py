"""Optional local orientation self-audit. It does not report completion or create a grade."""
import json
from pathlib import Path
CHECKS={"located_syllabus","located_schedule","opened_weekly_cards","read_safety_card","identified_support_routes","located_week1_handout"}
def load(path):
 with open(path,encoding="utf-8") as f:r=json.load(f)
 m=CHECKS.difference(r)
 if m:raise ValueError(f"Missing checks: {sorted(m)}")
 return r
def remaining(r):return sorted(k for k in CHECKS if r[k] is not True)
if __name__=="__main__":print("Remaining:",", ".join(remaining(load(Path(__file__).with_name("orientation_template.json")))))
