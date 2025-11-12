import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set data directory
DATA_DIR = Path(r"C:\Users\Administrator\Downloads\solar-challenge-week0\solar-challenge-week-0\data")

# Page title
st.title("☀️ Solar Data Dashboard")
st.markdown("Compare GHI, DNI, and DHI data across multiple countries.")

# Country files mapping
file_map = {
    "Benin": DATA_DIR / "benin-clean.csv",
    "Sierra Leone": DATA_DIR / "sierraleone-clean.csv",
    "Togo": DATA_DIR / "togo-clean.csv"
}

# Load all datasets into a dictionary
data_dict = {}
for country, path in file_map.items():
    df = pd.read_csv(path)
    
    # Ensure Timestamp column is datetime if exists
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    data_dict[country] = df

# Display dataset previews
st.write("### 📊 Dataset Previews")
for country, df in data_dict.items():
    st.write(f"#### {country}")
    st.dataframe(df.head())

# Plot boxplots for GHI, DNI, DHI side by side
st.write("### ☀️ Solar Irradiance Comparison (Boxplots)")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, col in enumerate(["GHI", "DNI", "DHI"]):
    box_data = [df[col].dropna() for df in data_dict.values()]
    axes[i].boxplot(box_data, labels=data_dict.keys())
    axes[i].set_title(f"{col} Distribution")
    axes[i].set_ylabel(col)

st.pyplot(fig)

# Optional: show top 5 GHI values for each country
st.write("### 🔝 Top 5 Highest GHI Values by Country")
for country, df in data_dict.items():
    if "GHI" in df.columns:
        top5 = df.nlargest(5, "GHI")[["GHI", "DNI", "DHI"]]
        st.write(f"#### {country}")
        st.table(top5)

# ---------------------------
# Interactive GHI Line Chart
# ---------------------------
st.write("### 📈 GHI Trend Over Time")

plt.figure(figsize=(12, 6))
for country, df in data_dict.items():
    if "Timestamp" in df.columns:
        plt.plot(df["Timestamp"], df["GHI"], label=country)
    else:
        plt.plot(df.index, df["GHI"], label=country)  # fallback to index

plt.xlabel("Time")
plt.ylabel("GHI")
plt.title("GHI Comparison Across Countries")
plt.legend()
plt.grid(True)
st.pyplot(plt.gcf())
