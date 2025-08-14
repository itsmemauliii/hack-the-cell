import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Hack the Cell", layout="centered")

st.title("🧬 Hack the Cell: Heavy Metal Biosensor Dashboard")
st.markdown("Upload biosensor readings to estimate contaminant levels.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    results = []
    for _, row in df.iterrows():
        payload = {
            "sample_id": row["SampleID"],
            "fluorescence": row["Fluorescence"],
            "growth": row["Growth"]
        }
        try:
            r = requests.post("http://localhost:8000/analyze", json=payload)
            results.append(r.json())
        except Exception as e:
            st.error(f"API request failed: {e}")

    if results:
        st.subheader("Analysis Results")
        st.dataframe(pd.DataFrame(results))
