-- ==========================================
-- Dimension Table: Fund
-- ==========================================

CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE NOT NULL,
    fund_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT,
    plan_type TEXT
);

-- ==========================================
-- Dimension Table: Date
-- ==========================================

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE NOT NULL,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER,
    weekday TEXT
);

-- ==========================================
-- Fact Table: NAV
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav_value REAL NOT NULL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- ==========================================
-- Fact Table: Transactions
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    investor_id TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    kyc_status TEXT,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- ==========================================
-- Fact Table: Performance
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

-- ==========================================
-- Fact Table: AUM
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    aum_crore REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);