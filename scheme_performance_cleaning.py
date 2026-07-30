import pandas as pd
import os

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# ---------------------------------
# Numeric columns to validate
# ---------------------------------
numeric_columns = [
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

print("\nValidating numeric columns...")

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------------------------
# Flag non-numeric / missing values
# ---------------------------------
anomalies = df[df[numeric_columns].isnull().any(axis=1)]

print("Anomalies Found:", len(anomalies))

# ---------------------------------
# Expense Ratio Validation
# Valid Range: 0.1% to 2.5%
# ---------------------------------
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:", len(invalid_expense))

# ---------------------------------
# Save cleaned dataset
# ---------------------------------
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/scheme_performance_clean.csv"

df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("Saved to:", output_file)