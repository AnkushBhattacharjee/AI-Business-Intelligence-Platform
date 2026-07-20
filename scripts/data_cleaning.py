from pathlib import Path
import pandas as pd

# Get project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Read dataset
csv_path = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"

df = pd.read_csv(csv_path, encoding="latin1")

print("=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)
print(df.head())

print("\n")

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(df.shape)

print("\n")

print("=" * 60)
print("COLUMN NAMES")
print("=" * 60)
print(df.columns)

print("\n")

print("=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

print("\n")
print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)
df.info()

print("\n")
print("=" * 60)
print("MISSING VALUES")
print("=" * 60)
missing_values = df.isnull().sum()
print(missing_values)

print("\n")
print("=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
duplicate_rows = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

print("\n")
print("=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)
print(df.describe())

print("\n")
print("=" * 60)
print("SALES BY CATEGORY")
print("=" * 60)
print(df.groupby("Category")["Sales"].sum())

print("\n")
print("=" * 60)
print("PROFIT BY CATEGORY")
print("=" * 60)
print(df.groupby("Category")["Profit"].sum())

print("\n")
print("=" * 60)
print("SALES BY REGION")
print("=" * 60)
print(df.groupby("Region")["Sales"].sum())

print("\n")
print("=" * 60)
print("PROFIT BY REGION")
print("=" * 60)
print(df.groupby("Region")["Profit"].sum())

print("\n")
print("=" * 60)
print("TOP CATEGORIES BY SALES")
print("=" * 60)
print(
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 60)
print("TOP STATES BY SALES")
print("=" * 60)
print(
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 60)
print("TOP CUSTOMERS BY SALES")
print("=" * 60)
print(
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n")
print("=" * 60)
print("FILTERING DATA")
print("=" * 60)

technology = df[df["Category"] == "Technology"]
print(technology)

high_profit = df[df["Profit"] > 100]
print(high_profit)

west = df[df["Region"] == "West"]
print(west)

high_sales = df[df["Sales"] > 500]
print(high_sales)

technology = df[df["Category"] == "Technology"]
print(technology["Sales"].sum())

print("\n")
print("=" * 60)
print("MULTIPLE GROUPING")
print("=" * 60)
print(df.groupby(["Category", "Region"])["Sales"].sum())
print(df.groupby(["Category", "Region"])["Profit"].sum())

print("\n")
print("=" * 60)
print("AGGREGATION")
print("=" * 60)
print(df.groupby("Category")["Sales"].agg(["sum", "mean", "max", "min"]))
print(df.groupby("Region")["Profit"].agg(["sum", "mean", "max", "min"]))

print("\n")
print("=" * 60)
print("PIVOT TABLES")
print("=" * 60)

sales_pivot = df.pivot_table(
    values="Sales",
    index="Category",
    columns="Region",
    aggfunc="sum"
)
print(sales_pivot)

profit_pivot = df.pivot_table(
    values="Profit",
    index="Category",
    columns="Region",
    aggfunc="sum"
)
print(profit_pivot)