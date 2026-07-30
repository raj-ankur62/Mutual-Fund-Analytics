import pandas as pd
import os

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# ---------------------------------
# 1. Fix transaction_date format
# ---------------------------------
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"], errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# ---------------------------------
# 2. Standardize transaction_type
# ---------------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Replace common variations
df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Lumpsum": "Lumpsum",
    "Redeem": "Redemption",
    "Redemption": "Redemption"
})

print("\nTransaction Type Values:")
print(df["transaction_type"].value_counts())

# ---------------------------------
# 3. Validate amount > 0
# ---------------------------------
invalid_amount = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Records:", len(invalid_amount))

# ---------------------------------
# 4. Check KYC Status
# ---------------------------------
valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid KYC Records:", len(invalid_kyc))

print("\nKYC Status Values:")
print(df["kyc_status"].value_counts())

# ---------------------------------
# Save cleaned dataset
# ---------------------------------
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/investor_transactions_clean.csv"

df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("Saved to:", output_file)