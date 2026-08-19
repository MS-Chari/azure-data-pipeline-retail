from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Synthetic retail input
INPUT_PATH = "/mnt/raw/retail_sales.csv"
OUTPUT_PATH = "/mnt/curated/retail_sales"

# Read raw data
raw_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(INPUT_PATH)
)

# Standardize column names and types
sales_df = (
    raw_df
    .withColumn("TransactionDate", F.to_date("TransactionDate"))
    .withColumn("TotalAmount", F.col("TotalAmount").cast("double"))
    .withColumn("Quantity", F.col("Quantity").cast("int"))
)

# Data-quality flags
validated_df = (
    sales_df
    .withColumn(
        "ValidationStatus",
        F.when(F.col("TransactionId").isNull(), "REJECT")
         .when(F.col("ProductId").isNull(), "REJECT")
         .when(F.col("TotalAmount") < 0, "REJECT")
         .when(F.col("TransactionDate").isNull(), "REJECT")
         .otherwise("VALID")
    )
)

# Keep valid records only
valid_df = validated_df.filter(F.col("ValidationStatus") == "VALID")

# Deduplicate by transaction ID, retaining the latest transaction date
window_spec = Window.partitionBy("TransactionId").orderBy(F.col("TransactionDate").desc())

curated_df = (
    valid_df
    .withColumn("row_num", F.row_number().over(window_spec))
    .filter(F.col("row_num") == 1)
    .drop("row_num")
    .withColumn("Profit", F.round(F.col("TotalAmount") * F.lit(0.25), 2))
    .withColumn(
        "SalesCategory",
        F.when(F.col("TotalAmount") >= 500, "High").otherwise("Normal")
    )
    .withColumn("IngestedAt", F.current_timestamp())
)

# Simple reporting aggregation
summary_df = (
    curated_df
    .groupBy("ProductId")
    .agg(
        F.sum("Quantity").alias("TotalQuantity"),
        F.round(F.sum("TotalAmount"), 2).alias("TotalSales"),
        F.round(F.sum("Profit"), 2).alias("TotalProfit")
    )
)

# Example output writes. Enable in a configured Databricks environment.
# curated_df.write.format("delta").mode("overwrite").save(OUTPUT_PATH)
# summary_df.write.format("delta").mode("overwrite").save(OUTPUT_PATH + "/summary")

print("Input rows:", raw_df.count())
print("Valid rows:", curated_df.count())
summary_df.show(20, truncate=False)
