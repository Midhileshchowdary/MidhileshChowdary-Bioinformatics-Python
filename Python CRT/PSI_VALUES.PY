# psi_analysis.py
# Raw PSI (Percent Spliced In) Data Analysis Script
# Author: Jyothi Sree
# Description: Performs quality filtering, statistical summary, and visualization of PSI values.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ---------------------------
# 1. Load the PSI Data
# ---------------------------
# Example file format: each row = splicing event, columns = samples
# First column = Event_ID, other columns = PSI values for each sample
file_path = r"C:/Users/hrjyo/Downloads/psi_values.csv"  # change to your file path
psi_data = pd.read_csv(file_path)

print("✅ Data loaded successfully!")
print(f"Shape: {psi_data.shape}")
print("\nPreview:")
print(psi_data.head())

# ---------------------------
# 2. Data Cleaning
# ---------------------------
# Remove rows with too many NaN values (e.g., missing PSI in >50% samples)
psi_clean = psi_data.dropna(thresh=int(psi_data.shape[1] * 0.5))
# Fill remaining NaNs with column mean
psi_clean = psi_clean.fillna(psi_clean.mean(numeric_only=True))

print(f"\nAfter cleaning: {psi_clean.shape[0]} events retained.")

# ---------------------------
# 3. Summary Statistics
# ---------------------------
psi_summary = psi_clean.describe()
print("\nSummary Statistics:")
print(psi_summary)

# Calculate mean PSI and variance per event
psi_clean["Mean_PSI"] = psi_clean.iloc[:, 1:].mean(axis=1)
psi_clean["Variance_PSI"] = psi_clean.iloc[:, 1:].var(axis=1)

# Identify highly variable events (potentially regulated splicing)
top_var_events = psi_clean.sort_values("Variance_PSI", ascending=False).head(10)
print("\nTop 10 Highly Variable Splicing Events:")
print(top_var_events[["Event_ID", "Mean_PSI", "Variance_PSI"]])

# ---------------------------
# 4. Visualization
# ---------------------------

# (a) PSI Distribution per sample
plt.figure(figsize=(10, 5))
sns.boxplot(data=psi_clean.iloc[:, 1:-2])
plt.title("PSI Distribution Across Samples")
plt.xlabel("Samples")
plt.ylabel("PSI (Percent Spliced In)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (b) Histogram of mean PSI values
plt.figure(figsize=(7, 5))
sns.histplot(psi_clean["Mean_PSI"], bins=30, kde=True)
plt.title("Distribution of Mean PSI Across Events")
plt.xlabel("Mean PSI")
plt.ylabel("Frequency")
plt.show()

# (c) Correlation heatmap between samples
plt.figure(figsize=(8, 6))
sns.heatmap(psi_clean.iloc[:, 1:-2].corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Between Samples Based on PSI Values")
plt.tight_layout()
plt.show()

# ---------------------------
# 5. Optional: Statistical Testing
# ---------------------------
# Example: compare PSI between two conditions (if you have sample groups)
# Suppose columns: ["Event_ID", "Sample1", "Sample2", "Sample3", "Sample4"]
# And Sample1–2 = condition A, Sample3–4 = condition B

# Define groups (update with actual column names)
condition_A = psi_clean[["Sample1", "Sample2"]]
condition_B = psi_clean[["Sample3", "Sample4"]]

# Perform t-test per event (example)
psi_clean["p_value"] = psi_clean.apply(
    lambda row: stats.ttest_ind(
        row[["Sample1", "Sample2"]],
        row[["Sample3", "Sample4"]],
        equal_var=False,
        nan_policy="omit"
    ).pvalue,
    axis=1
)

# Adjust for multiple testing (Benjamini-Hochberg FDR)
psi_clean = psi_clean.sort_values("p_value")
print("\nTop Differentially Spliced Events (by p-value):")
print(psi_clean[["Event_ID", "p_value"]].head(10))
