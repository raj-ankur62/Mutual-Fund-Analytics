"""
Data Cleaning Module

This script cleans and processes all Mutual Fund Analytics datasets.

General processing:
1. Loads raw CSV datasets
2. Standardizes column names
3. Removes duplicate records
4. Handles missing values
5. Cleans text columns
6. Saves processed datasets

Additional NAV processing:
1. Converts the date column
2. Sorts data by AMFI code and date
3. Removes invalid NAV values
"""



import pandas as pd
import os


def clean_nav_data(df):
    """
    Clean and validate NAV history data.

    Parameters:
        df (pd.DataFrame): Raw NAV history dataset.

    Returns:
        pd.DataFrame: Cleaned NAV dataset.
    """

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.sort_values(["amfi_code", "date"])
    df = df.drop_duplicates()
    df = df[df["nav"] > 0]

    return df


raw_folder = "data/raw/"
processed_folder = "data/processed/"

os.makedirs(processed_folder, exist_ok=True)


files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]


for file in files:

    print(f"\nCleaning: {file}")

    df = pd.read_csv(raw_folder + file)

    # Clean column names first
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Apply NAV-specific cleaning
    if file == "02_nav_history.csv":
        df = clean_nav_data(df)

    else:
        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Handle missing values
        for col in df.columns:

            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
                df[col] = df[col].str.strip()

            else:
                df[col] = df[col].fillna(0)

    # Save cleaned file
    output_file = file.replace(".csv", "_clean.csv")

    df.to_csv(
        processed_folder + output_file,
        index=False
    )

    print(f"Saved: {output_file}")


print("\nAll CSV Cleaning Completed Successfully")