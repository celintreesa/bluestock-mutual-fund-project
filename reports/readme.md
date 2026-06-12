# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview
This project analyzes mutual fund data using Python, SQLite, and Power BI. The objective is to build an end-to-end analytics pipeline for mutual fund performance evaluation, investor transaction analysis, and risk assessment.

## Data Sources
- Fund Master Data
- NAV History
- AUM Data
- SIP Inflows
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

## Project Structure
data/raw - Source datasets

data/processed - Cleaned datasets

sql - Database schema and SQL scripts

dashboards - Power BI dashboard

notebooks - Analysis notebooks

reports - Final report and presentation

## Installation

```bash
pip install -r requirements.txt

## Running the ETL Pipeline

python run_pipeline.py

## Database

SQLite database: bluestock_mf.db

## Dashboard

Open bluestock_mf.pbix using Power BI Desktop.

## Analysis Performed

- Exploratory Data Analysis
- Performance Analysis
- Sharpe Ratio Analysis
- VaR & CVaR Analysis
- Cohort Analysis
- SIP Continuity Analysis
- Sector Concentration Analysis

## Outputs

- sharpe_ratio.csv
- var_cvar_report.csv
- sector_hhi.csv
- sip_continuity_report.csv
- cohort_analysis.csv

## Author

Celin Treesa