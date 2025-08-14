import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hack the Cell", layout="centered")

st.title("🧬 Hack the Cell: Heavy Metal Biosensor Dashboard")
st.markdown("Upload biosensor readings to estimate contaminant levels.")

# Example data for default view
example_data = pd.DataFrame({
    "SampleID": [1, 2, 3, 4],
    "Fluorescence": [150, 300, 500, 900],
    "Growth": [0.95, 0.92, 0.85, 0.70]
})

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded — using example dataset.")
    df = example_data

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

required_cols = {"sampleid", "fluorescence", "growth"}
if required_cols.issubset(df.columns):
    st.subheader("Data Being Analyzed")
    st.dataframe(df)

    results = []
    for _, row in df.iterrows():
        # Parameters for Hill equation
        F_min, F_max, K_d, n = 100, 1000, 0.5, 2.0

        # Estimate concentration
        conc = ((row["fluorescence"] - F_min) * (K_d ** n) /
                ((F_max - row["fluorescence"]) ** (1/n)))
        conc = abs(conc)

        # Safety check
        status = "Safe" if conc < 0.3 else "Unsafe"

        results.append({
            "sample_id": row["sampleid"],
            "estimated_metal_concentration": round(conc, 4),
            "status": status
        })

    st.subheader("Analysis Results")
    st.dataframe(pd.DataFrame(results))
else:
    st.error("CSV must contain columns: SampleID, Fluorescence, Growth")
