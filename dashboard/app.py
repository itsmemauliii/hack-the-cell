import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hack the Cell", layout="centered")

st.title("🧬 Hack the Cell: Heavy Metal Biosensor Dashboard")
st.markdown("Upload biosensor readings to estimate contaminant levels.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df)

    results = []
    for _, row in df.iterrows():
        # Parameters for Hill equation
        F_min, F_max, K_d, n = 100, 1000, 0.5, 2.0

        # Estimate concentration (simple biosensor model)
        conc = ((row["Fluorescence"] - F_min) * (K_d ** n) /
                ((F_max - row["Fluorescence"]) ** (1/n)))
        conc = abs(conc)

        # Safety threshold
        status = "Safe" if conc < 0.3 else "Unsafe"

        results.append({
            "sample_id": row["SampleID"],
            "estimated_metal_concentration": round(conc, 4),
            "status": status
        })

    if results:
        st.subheader("Analysis Results")
        st.dataframe(pd.DataFrame(results))
