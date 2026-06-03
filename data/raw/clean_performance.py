import pandas as pd

# Read file
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert expense ratio to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Keep expense ratio between 0.1 and 2.5
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Flag anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("Anomalies Found:", len(anomalies))

# Save anomalies
anomalies.to_csv(
    "data/processed/performance_anomalies.csv",
    index=False
)

# Save cleaned data
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance cleaned successfully!")
print("Total rows:", len(df))