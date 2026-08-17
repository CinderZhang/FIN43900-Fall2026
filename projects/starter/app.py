"""Minimal Streamlit shell. It intentionally contains no completed finance analysis."""
from __future__ import annotations
import json
from pathlib import Path
import streamlit as st

OUTPUT = Path(__file__).with_name("visible_output.json")
st.set_page_config(page_title="FIN 43900 Decision System", layout="wide")
st.title("Finance Decision System")
st.caption("Student project shell — replace placeholders with tested, traceable evidence.")

if OUTPUT.exists():
    record = json.loads(OUTPUT.read_text(encoding="utf-8"))
    st.subheader(record.get("decision", "Decision not yet defined"))
    st.write("As of:", record.get("as_of", "not set"))
    st.write("Recommendation:", record.get("recommendation", "not set"))
    st.write("Reversal trigger:", record.get("reversal_trigger", "not set"))
else:
    st.warning("No visible_output.json exists. Run and validate the student analysis first.")

st.info("The interface cannot establish finance quality; inspect sources, conventions, tests, and the frozen validation record.")
