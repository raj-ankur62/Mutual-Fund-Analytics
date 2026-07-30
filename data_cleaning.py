import pandas as pd
import os

print("Current Working Directory:", os.getcwd())

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# 1. Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["date"])

# 2. Sort by AMFI Code and Date
df = df.sort_values(by=["amfi_code", "date"])

# 3. Remove duplicate records
before = len(df)
df = df.drop_duplicates(subset=["amfi_code", "date"], keep="last")
print("Duplicates Removed:", before - len(df))

# 4. Forward-fill missing NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# 5. Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

if invalid_nav.empty:
    print("✅ All NAV values are greater than 0.")
else:
    print("❌ Invalid NAV records found:")
    print(invalid_nav)

# Remove remaining missing NAV values
df = df.dropna(subset=["nav"])

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
output_file = "data/processed/nav_history_clean.csv"
df.to_csv(output_file, index=False)

print("\nCleaning completed successfully!")
print("Final Shape:", df.shape)
print("Saved to:", output_file)