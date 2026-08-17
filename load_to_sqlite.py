import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path


# Create SQLite database
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

# Cleaned datasets
datasets = {
    "nav_history": "data/processed/02_nav_history_clean.csv",
    "investor_transactions": "data/processed/08_investor_transactions_clean.csv",
    "scheme_performance": "data/processed/07_scheme_performance_clean.csv"
}

print("=" * 60)
print("Loading Cleaned Datasets into SQLite")
print("=" * 60)

for table_name, file_path in datasets.items():

    print(f"\nLoading table: {table_name}")

    # Read CSV
    df = pd.read_csv(file_path)

    # Load data into SQLite
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    # Verify row count
    with engine.connect() as conn:
        db_count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table_name}")
        ).scalar()

    csv_count = len(df)

    print(f"CSV Rows    : {csv_count}")
    print(f"SQLite Rows : {db_count}")

    if csv_count == db_count:
        print("✅ Row count matched")
    else:
        print("❌ Row count mismatch")

print("\nAll datasets loaded successfully!")