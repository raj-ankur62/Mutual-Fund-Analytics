import requests
import pandas as pd
import os
import json

# API URL
url = "https://api.mfapi.in/mf/125497"

# Fetch data from API
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:

    # Convert JSON response to Python dictionary
    json_data = response.json()

    # Extract metadata
    meta = json_data["meta"]

    print("=" * 60)
    print("Scheme Name :", meta["scheme_name"])
    print("Scheme Code :", meta["scheme_code"])
    print("=" * 60)

    # Convert NAV data into DataFrame
    df = pd.DataFrame(json_data["data"])

    print("\nDataset Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    # Create folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save CSV
    output_file = "data/raw/SBI_Small_Cap_NAV.csv"
    df.to_csv(output_file, index=False)

    print(f"\nCSV saved successfully: {output_file}")

else:
    print("API Request Failed:", response.status_code)


    json_data = response.json()



# Create raw data folder
os.makedirs("data/raw", exist_ok=True)

# Save complete JSON response
with open("data/raw/SBI_Small_Cap_NAV.json", "w") as file:
    json.dump(json_data, file, indent=4)

print("JSON file saved successfully.")






# Historical CSV load
historical_df = pd.read_csv(
    "data/raw/SBI_Small_Cap_NAV.csv"
)

print("Historical Dataset:")
print(historical_df.head())
print(historical_df.shape)


# JSON Load
with open("data/raw/SBI_Small_Cap_NAV.json", "r") as file:
    api_data = json.load(file)


# YAHAN CODE RAKHNA HAI
api_df = pd.DataFrame(api_data["data"])


print("API Dataset:")
print(api_df.head())
print(api_df.shape)


# Data type conversion
historical_df["date"] = pd.to_datetime(
    historical_df["date"],
    format="%d-%m-%Y"
)

historical_df["nav"] = historical_df["nav"].astype(float)


api_df["date"] = pd.to_datetime(
    api_df["date"],
    format="%d-%m-%Y"
)

api_df["nav"] = api_df["nav"].astype(float)

comparison_df = historical_df.merge(
    api_df,
    on="date",
    how="outer",
    suffixes=("_historical", "_api")
)

print("Comparison Dataset:")
print(comparison_df.head())
print(comparison_df.shape)

comparison_df["difference"] = (
    comparison_df["nav_historical"] -
    comparison_df["nav_api"]
)

print(comparison_df.head())


## mismatch check
mismatch = comparison_df[
    comparison_df["difference"] != 0
]

print("Mismatch Records:")
print(mismatch)
print("Total Mismatches:", len(mismatch))


## Comparison report

comparison_df.to_csv(
    "data/processed/NAV_comparison_report.csv",
    index=False
)

print("Comparison report saved successfully.")