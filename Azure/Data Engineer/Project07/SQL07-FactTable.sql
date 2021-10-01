-- Lab - Building a Fact Table
-- Lets first create a view

  CREATE VIEW [Sales_Fact_View]
  AS
  SELECT dt.[ProductID],dt.[SalesOrderID],dt.[OrderQty],dt.[UnitPrice],hd.[OrderDate],hd.[CustomerID],hd.[TaxAmt]
  FROM [Sales].[SalesOrderDetail] dt
  LEFT JOIN [Sales].[SalesOrderHeader] hd
  ON dt.[SalesOrderID]=hd.[SalesOrderID]

-- Then we will create the Sales Fact table from the view
  
SELECT [ProductID],[SalesOrderID],[CustomerID],[OrderQty],[UnitPrice],[OrderDate],[TaxAmt]
INTO SalesFact
FROM Sales_Fact_View


-- Lab - Building a dimension table
-- Lets build a view for the customers

CREATE VIEW Customer_view 
AS
  SELECT ct.[CustomerID],ct.[StoreID],st.[BusinessEntityID],st.[Name]  as StoreName
  FROM [Sales].[Customer] as ct
  LEFT JOIN [Sales].[Store] as st 
  ON ct.[StoreID]=st.[BusinessEntityID]
  WHERE  st.[BusinessEntityID] IS NOT NULL

-- Lets create a customer dimension table

SELECT [CustomerID],[StoreID],[BusinessEntityID],StoreName
INTO DimCustomer
FROM Customer_view 


-- Lets build a view for the products

CREATE VIEW Product_view 
AS
SELECT prod.[ProductID],prod.[Name] as ProductName,prod.[SafetyStockLevel],model.[ProductModelID],model.[Name] as ProductModelName,category.[ProductSubcategoryID],category.[Name] AS ProductSubCategoryName
FROM [Production].[Product] prod
LEFT JOIN [Production].[ProductModel] model ON prod.[ProductModelID] = model.[ProductModelID]
LEFT JOIN [Production].[ProductSubcategory] category ON prod.[ProductSubcategoryID]=category.[ProductSubcategoryID]
WHERE prod.[ProductModelID] IS NOT NULL

-- Lets create a product dimension table

SELECT [ProductID],[ProductModelID],[ProductSubcategoryID],ProductName,[SafetyStockLevel],ProductModelName,ProductSubCategoryName
INTO DimProduct
FROM Product_view 

-- If you want to drop the views and the tables

DROP VIEW Customer_view 

DROP TABLE DimCustomer

DROP VIEW Product_view 

DROP TABLE DimProduct

-- This is just a sample query that can be used to join both the Dimension and the Fact table

SELECT dimc.StoreName,dimp.ProductName,dimp.ProductSubCategoryName,SUM(ft.OrderQty) AS Quantity
FROM SalesFact ft
INNER JOIN DimCustomer dimc ON ft.CustomerID=dimc.CustomerID
INNER JOIN DimProduct dimp ON ft.ProductID=dimp.ProductID
GROUP BY dimc.StoreName,dimp.ProductName,dimp.ProductSubCategoryName

-- Lab - Transfer data to our SQL Pool

-- First let's ensure we have the tables defined in the SQL pool

CREATE TABLE [dbo].[SalesFact](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)


CREATE TABLE [dbo].[DimCustomer](
	[CustomerID] [int] NOT NULL,
	[StoreID] [int] NOT NULL,
	[BusinessEntityID] [int] NOT NULL,
	[StoreName] varchar(50) NOT NULL
)


CREATE TABLE [dbo].[DimProduct](
	[ProductID] [int] NOT NULL,
	[ProductModelID] [int] NOT NULL,
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductName] varchar(50) NOT NULL,
	[SafetyStockLevel] [smallint] NOT NULL,
	[ProductModelName] varchar(50) NULL,
	[ProductSubCategoryName] varchar(50) NULL
)

SELECT * FROM [dbo].[SalesFact]
SELECT COUNT(*) FROM [dbo].[SalesFact]

SELECT * FROM [dbo].[DimCustomer]
SELECT COUNT(*) FROM [dbo].[DimCustomer]

SELECT * FROM [dbo].[DimProduct]
SELECT COUNT(*) FROM [dbo].[DimProduct]

-- If we need to drop the tables

DROP TABLE [dbo].[SalesFact]

DROP TABLE [dbo].[DimCustomer]

DROP TABLE [dbo].[DimProduct]


-- Lab - Creating Round-robin Tables

-- First let's ensure we have the tables defined in the SQL pool
-- We will use Azure Data Factory to transfer the tables

CREATE TABLE [dbo].[SalesFact](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)


-- To see the distribution on the table
DBCC PDW_SHOWSPACEUSED('[dbo].[SalesFact]')

-- If you execute the below query
SELECT [CustomerID], COUNT([CustomerID]) as COUNT FROM [dbo].[SalesFact]
GROUP BY [CustomerID]
ORDER BY [CustomerID]


-- Lab - Creating Hash-distributed Tables

-- Let's drop the existing table

DROP TABLE [dbo].[SalesFact]

-- Now we want to create a hash-distributed table and set the hash-based column as the Customer ID

CREATE TABLE [dbo].[SalesFact](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)
WITH  
(   
    DISTRIBUTION = HASH (CustomerID)
)

-- To see the distribution on the table
DBCC PDW_SHOWSPACEUSED('[dbo].[SalesFact]')

-- If you execute the below query
SELECT [CustomerID], COUNT([CustomerID]) as COUNT FROM [dbo].[SalesFact]
GROUP BY [CustomerID]
ORDER BY [CustomerID]

-- Lab - Creating Replicated Tables

-- Let's drop the existing table

DROP TABLE [dbo].[SalesFact]

-- Now we want to create a hash-distributed table and set the hash-based column as the Customer ID

CREATE TABLE [dbo].[SalesFact](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)
WITH  
(   
    DISTRIBUTION = REPLICATE
)

-- To see the distribution on the table
DBCC PDW_SHOWSPACEUSED('[dbo].[SalesFact]')

-- If you execute the below query
SELECT [CustomerID], COUNT([CustomerID]) as COUNT FROM [dbo].[SalesFact]
GROUP BY [CustomerID]
ORDER BY [CustomerID]

-- Lab - Windowing Functions

SELECT
ROW_NUMBER() OVER(PARTITION BY [ProductID] ORDER BY [OrderQty]) AS "Row Number",
[ProductID],[CustomerID],[OrderQty],[UnitPrice]
FROM [dbo].[SalesFact]
ORDER BY [ProductID]

SELECT
ROW_NUMBER() OVER(PARTITION BY [ProductID] ORDER BY [OrderQty]) AS "Row Number",
[ProductID],[CustomerID],[OrderQty],
SUM([OrderQty]) OVER(PARTITION BY [ProductID]) AS TotalOrderQty,
[UnitPrice]
FROM [dbo].[SalesFact]
ORDER BY [ProductID]


-- Lab - Surrogate keys for dimension tables

-- First let's ensure we have the tables defined in the SQL pool
-- Let's do this for one dimension table

-- First drop the table if you have it in place

DROP TABLE [dbo].[DimProduct]

CREATE TABLE [dbo].[DimProduct](
	[ProductSK] [int] IDENTITY(1,1) NOT NULL,
	[ProductID] [int] NOT NULL,
	[ProductModelID] [int] NOT NULL,
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductName] varchar(50) NOT NULL,
	[SafetyStockLevel] [smallint] NOT NULL,
	[ProductModelName] varchar(50) NULL,
	[ProductSubCategoryName] varchar(50) NULL
)



-- Lab - CASE statement

CREATE TABLE [ProductDetails]
(
   [productid] int,
   [productname] varchar(20),
   [productstatus] varchar(1),
   [quantity] int
)


SELECT [productid],[productname],
status = CASE [productstatus]
WHEN 'W' THEN 'Warehouse'
WHEN 'S' THEN 'Store'
WHEN 'T' THEN 'Transit'
END
FROM [ProductDetails]

-- Lab - Example when using the right distributions for your tables

DROP TABLE [dbo].[SalesFact]


CREATE TABLE [dbo].[SalesFact](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)
WITH  
(   
    DISTRIBUTION = HASH (ProductID)
)

-- Create the dimension table with round-robin distribution

DROP TABLE [dbo].[DimProduct]

CREATE TABLE [dbo].[DimProduct](
	[ProductID] [int] NOT NULL,
	[ProductModelID] [int] NOT NULL,
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductName] varchar(50) NOT NULL,
	[SafetyStockLevel] [smallint] NOT NULL,
	[ProductModelName] varchar(50) NULL,
	[ProductSubCategoryName] varchar(50) NULL
)

-- Perform a JOIN on the fact and dimension table

SELECT ft.[ProductID],pd.[ProductName]
FROM [dbo].[SalesFact] ft JOIN [dbo].[DimProduct] pd
ON  ft.[ProductID]=pd.[ProductID]


-- Create the dimension table with replicated distribution

DROP TABLE [dbo].[DimProduct]

CREATE TABLE [dbo].[DimProduct](
	[ProductID] [int] NOT NULL,
	[ProductModelID] [int] NOT NULL,
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductName] varchar(50) NOT NULL,
	[SafetyStockLevel] [smallint] NOT NULL,
	[ProductModelName] varchar(50) NULL,
	[ProductSubCategoryName] varchar(50) NULL
)
WITH  
(   
    DISTRIBUTION = REPLICATE
)


-- Creating a heap table

CREATE TABLE [dbo].[SalesFact_staging](
	[ProductID] [int] NOT NULL,
	[SalesOrderID] [int] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[OrderDate] [datetime] NULL,
	[TaxAmt] [money] NULL
)
WITH(HEAP,
DISTRIBUTION = ROUND_ROBIN
)

CREATE INDEX ProductIDIndex ON [dbo].[SalesFact_staging] (ProductID)



