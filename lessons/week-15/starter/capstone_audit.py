"""Structural evidence-graph checks; finance judgment remains human-owned."""
from pathlib import Path
import pandas as pd
REQ={"claim_id","decision_use","component","input_source","as_of_date","convention","calculation_or_output","validation_test","test_result","owner","reversal_trigger"}
def load(path):
 d=pd.read_csv(path,keep_default_na=False);m=REQ.difference(d.columns)
 if m:raise ValueError(f"Missing columns: {sorted(m)}")
 return d
def row_gaps(d):return {r.claim_id:[c for c in REQ if not getattr(r,c)] for r in d.itertuples(index=False)}
def detect_financial_contradictions(d):raise NotImplementedError("Semantic contradictions require evidence-aware review")
if __name__=="__main__":print(row_gaps(load(Path(__file__).with_name("evidence_graph_template.csv"))))
