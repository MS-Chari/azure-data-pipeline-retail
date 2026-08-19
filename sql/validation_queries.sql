-- Duplicate transaction IDs
SELECT TransactionId, COUNT(*) AS DuplicateCount
FROM dbo.RetailSales
GROUP BY TransactionId
HAVING COUNT(*) > 1;

-- Invalid negative sales
SELECT *
FROM dbo.RetailSales
WHERE TotalAmount < 0;

-- Missing required fields
SELECT *
FROM dbo.RetailSales
WHERE TransactionId IS NULL
   OR ProductId IS NULL
   OR TransactionDate IS NULL;

-- Daily sales reconciliation
SELECT
    TransactionDate,
    COUNT(*) AS TransactionCount,
    SUM(TotalAmount) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM dbo.RetailSales
GROUP BY TransactionDate
ORDER BY TransactionDate;

-- Top products by sales
SELECT TOP 10
    ProductId,
    SUM(Quantity) AS TotalQuantity,
    SUM(TotalAmount) AS TotalSales
FROM dbo.RetailSales
GROUP BY ProductId
ORDER BY TotalSales DESC;
