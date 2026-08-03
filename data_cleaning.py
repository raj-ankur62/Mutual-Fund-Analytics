import pandas as pd
import os


raw_folder = "data/raw/"
processed_folder = "data/processed/"


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

    print("\nCleaning:", file)

    df = pd.read_csv(raw_folder + file)


    # Remove duplicates
    df.drop_duplicates(inplace=True)


    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    # Handle missing values
    for col in df.columns:

        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
            df[col] = df[col].str.strip()

        else:
            df[col] = df[col].fillna(0)


    # Save file

    output_file = file.replace(".csv", "_clean.csv")


    df.to_csv(
        processed_folder + output_file,
        index=False
    )


    print("Saved:", output_file)


print("All CSV Cleaning Completed")