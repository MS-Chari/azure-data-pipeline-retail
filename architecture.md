# Architecture – Azure Retail Data Pipeline

## High-Level Design

```text
                    +----------------------+
                    | Synthetic CSV Data   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | ADLS Gen2 / Blob Raw  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Azure Data Factory    |
                    | - Parameters          |
                    | - Copy Activity      |
                    | - Validation          |
                    | - Orchestration       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Azure Databricks      |
                    | PySpark               |
                    | - Clean               |
                    | - Validate            |
                    | - Deduplicate         |
                    | - Transform           |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Curated Data Layer    |
                    | Delta / Azure SQL     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Power BI              |
                    +----------------------+
```

## Layer Responsibilities

| Layer | Responsibility |
|---|---|
| Raw | Preserve source files without business transformation |
| ADF | Orchestrate ingestion and pipeline dependencies |
| Databricks | Perform scalable PySpark transformation and quality checks |
| Curated | Store clean, analytics-ready data |
| Power BI | Consume curated data for reporting |

## Design Principles

- Parameterized ingestion
- Separation of raw and curated data
- Reusable orchestration
- Data-quality validation before publication
- Incremental processing using a watermark pattern
- Synthetic data only for portfolio demonstration
