import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Hack the Cell", layout="centered")

st.title("🧬 Hack the Cell: Heavy Metal Biosensor Dashboard")
st.markdown("Upload biosensor readings to estimate contaminant levels.")

# Example dataset
example_data = pd.DataFrame({
    "SampleID": [1, 2, 3, 4],
    "Fluorescence": [150, 300, 500, 900],
    "Growth": [0.95, 0.92, 0.85, 0.70]
})

# File upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# Load data
try:
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ CSV uploaded successfully!")
    else:
        st.info("ℹ️ No file uploaded — using example dataset.")
        df = example_data
except Exception as e:
    st.error(f"Error reading file: {e}")
    df = example_data

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check required columns
required_cols = {"sampleid", "fluorescence", "growth"}
if not required_cols.issubset(df.columns):
    st.error(f"CSV must contain columns: {required_cols}")
    st.stop()

# Ensure numeric types
for col in ["fluorescence", "growth"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop NaN rows
df = df.dropna(subset=["fluorescence", "growth"])

# Display input data
st.subheader("📊 Data Being Analyzed")
st.dataframe(df)

# Hill equation parameters
F_min, F_max, K_d, n = 100, 1000, 0.5, 2.0

# Calculate results
results = []
for _, row in df.iterrows():
    try:
        if row["fluorescence"] >= F_max:
            conc = np.nan  # avoid division by zero
        else:
            conc = ((row["fluorescence"] - F_min) * (K_d ** n) /
                    ((F_max - row["fluorescence"]) ** (1/n)))
        conc = abs(conc) if pd.notna(conc) else np.nan
        status = "Safe" if conc < 0.3 else "Unsafe"
        results.append({
            "sample_id": row["sampleid"],
            "estimated_metal_concentration": round(conc, 4) if pd.notna(conc) else None,
            "status": status if pd.notna(conc) else "Invalid Reading"
        })
    except Exception as e:
        st.warning(f"Error processing sample {row['sampleid']}: {e}")

# Show results
if results:
    st.subheader("✅ Analysis Results")
    st.dataframe(pd.DataFrame(results))
else:
    st.warning("⚠️ No valid results to display.")
