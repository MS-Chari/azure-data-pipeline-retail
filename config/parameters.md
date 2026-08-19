# ADF Pipeline Parameters

Suggested parameters for a reusable ingestion pipeline:

| Parameter | Example | Purpose |
|---|---|---|
| `sourceFileName` | `retail_sales_2026_08_19.csv` | Identifies the incoming file |
| `sourceFolder` | `raw/retail` | Landing folder |
| `targetTable` | `dbo.RetailSales` | Curated SQL target |
| `watermarkDate` | `2026-08-18` | Start point for incremental processing |
| `batchId` | `20260819001` | Traceability across the run |

## Recommended Pipeline Sequence

1. Receive parameters.
2. Validate source file availability.
3. Read the current watermark.
4. Copy the raw file to the landing/processing area.
5. Execute Databricks transformation.
6. Validate output counts.
7. Load the curated target.
8. Update the watermark only after successful completion.
9. Write audit status.
