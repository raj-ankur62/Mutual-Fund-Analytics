import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Database path
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

# SQL schema path
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

# Create database connection
conn = sqlite3.connect(DB_PATH)

# Execute schema
with open(SCHEMA_PATH, "r") as f:
    conn.executescript(f.read())

conn.close()

print("Database schema created successfully!")