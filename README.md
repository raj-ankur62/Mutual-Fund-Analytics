# Mutual Fund Analytics

## Project Overview

This project is an end-to-end Mutual Fund Analytics project that analyzes mutual fund performance, risk, investor behavior, portfolio concentration, and market trends.

The project includes:

- Data ingestion and validation
- Data cleaning and transformation
- SQLite database and SQL analysis
- Exploratory Data Analysis (EDA)
- Fund performance analytics
- Risk analytics
- Investor analytics
- Fund recommendation
- Interactive Power BI dashboard

The analysis covers **40 mutual fund schemes** using datasets related to NAV, AUM, SIP inflows, investor transactions, portfolio holdings, scheme performance, and benchmark indices.

## Project Architecture

```text
Data Sources
     |
     v
Python Data Ingestion
     |
     v
Data Cleaning & Validation
     |
     v
Processed CSV Files
     |
     v
SQLite Database
     |
     v
EDA + Performance & Risk Analytics
     |
     v
Power BI Dashboard
     |
     v
Insights & Final Report

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/raj-ankur62/Mutual-Fund-Analytics.git
cd Mutual-Fund-Analytics

2. Create a Virtual Environment
python -m venv venv

3. Activate the Virtual Environment
venv\Scripts\activate

4. Install Required Libraries
pip install -r requirements.txt
```

## Author

Ankur Kumar