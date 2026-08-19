# Azure Data Engineering Pipeline – Retail Sales

An end-to-end **Azure Data Engineering portfolio project** demonstrating ingestion, transformation, validation, incremental processing, and analytics using synthetic retail data.

> **Portfolio disclaimer:** This repository contains synthetic/demo data only. It does not contain employer/client data, credentials, proprietary logic, or confidential code.

## Architecture

```text
Synthetic CSV Files
        |
        v
Azure Blob Storage / ADLS Gen2
        |
        v
Azure Data Factory
  |     |       |
Copy  Validation  Parameters
        |
        v
Azure Databricks / PySpark
  |     |       |
Clean  Transform  Aggregate
        |
        v
Curated Delta / SQL Layer
        |
        v
Power BI / Analytics
```

## Technologies
- Azure Data Factory (ADF)
- Azure Databricks
- PySpark
- ADLS Gen2 / Azure Blob Storage
- Azure SQL Database
- Delta Lake concepts
- Power BI
- Python / SQL

## Data Flow
1. ADF receives a parameterized source file name and ingestion date.
2. Source data is copied from the raw landing zone.
3. Basic quality checks identify missing IDs, invalid amounts, and duplicate records.
4. Databricks reads the raw data and applies PySpark transformations.
5. Derived measures such as `Profit` and `SalesCategory` are created.
6. Data is written to a curated layer for reporting.
7. Audit metrics capture input, valid, rejected, and output row counts.

## Incremental Load Approach
The project demonstrates a watermark-style pattern using `TransactionDate` and `TransactionId`.

- First run: process the available historical dataset.
- Subsequent runs: process only records newer than the stored watermark.
- Duplicate transaction IDs are removed before the curated load.

## Validation Rules
- Transaction ID must not be null.
- Product ID must not be null.
- Transaction amount must be greater than or equal to zero.
- Transaction date must be present and valid.
- Duplicate transaction IDs are rejected/deduplicated.

## Repository Structure

```text
README.md
architecture.md
notebooks/
  databricks_transformations.py
pipelines/
  adf_pipeline.json
sql/
  create_retail_schema.sql
  validation_queries.sql
sample_data/
  retail_sales.csv
config/
  parameters.md
```

## Portfolio Highlights

### Example 1 – ADF
A parameterized pipeline pattern separates ingestion from transformation and supports reusable source/sink configuration.

### Example 2 – Databricks
PySpark performs data-quality checks, deduplication, derived columns, and aggregations before the reporting layer.

## What This Demonstrates
This project is intentionally designed to show practical Data Engineer skills rather than a collection of disconnected code snippets: **ADF orchestration + Databricks/PySpark transformation + SQL data modeling + data quality + incremental processing**.
