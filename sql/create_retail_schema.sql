CREATE TABLE dbo.RetailSales (
    TransactionId VARCHAR(50) NOT NULL,
    TransactionDate DATE NOT NULL,
    ProductId VARCHAR(50) NOT NULL,
    Quantity INT NULL,
    TotalAmount DECIMAL(18,2) NOT NULL,
    Profit DECIMAL(18,2) NULL,
    SalesCategory VARCHAR(20) NULL,
    IngestedAt DATETIME2 NULL,
    CONSTRAINT PK_RetailSales PRIMARY KEY (TransactionId)
);

CREATE TABLE dbo.RetailPipelineAudit (
    BatchId BIGINT NOT NULL,
    PipelineName VARCHAR(200) NOT NULL,
    StartTime DATETIME2 NOT NULL,
    EndTime DATETIME2 NULL,
    SourceRows INT NULL,
    ValidRows INT NULL,
    RejectedRows INT NULL,
    TargetRows INT NULL,
    Status VARCHAR(20) NOT NULL,
    ErrorMessage VARCHAR(2000) NULL
);

CREATE TABLE dbo.RetailWatermark (
    PipelineName VARCHAR(200) NOT NULL PRIMARY KEY,
    LastTransactionDate DATE NULL,
    LastTransactionId VARCHAR(50) NULL,
    UpdatedAt DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
