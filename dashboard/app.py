import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Hack the Cell Dashboard", layout="wide")

st.title("Hack the Cell - Biosensor Results")
st.write("Upload biosensor readings and get real-time analysis.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data", df)

    results = []
    for _, row in df.iterrows():
        payload = {
            "sample_id": str(row["SampleID"]),
            "fluorescence": float(row["Fluorescence"]),
            "growth": float(row["Growth"])
        }
        r = requests.post("http://localhost:8000/analyze", json=payload)
        results.append(r.json())

    results_df = pd.DataFrame(results)
    st.write("Analysis Results", results_df)
