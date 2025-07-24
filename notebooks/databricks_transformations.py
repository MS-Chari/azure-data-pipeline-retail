# Databricks Notebook: Transform Retail Sales Data
from pyspark.sql.functions import col, when

# Read the CSV file
df = spark.read.csv("/mnt/raw/retail_sales.csv", header=True, inferSchema=True)

# Add Profit and SalesCategory
df = df.withColumn("Profit", col("TotalAmount") * 0.25)       .withColumn("SalesCategory", when(col("TotalAmount") > 500, "High").otherwise("Normal"))

df.show()
