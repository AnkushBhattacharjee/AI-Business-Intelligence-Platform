from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"
df = pd.read_csv(csv_path, encoding="latin1")

category_sales = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))

bars = plt.bar(
    category_sales.index,
    category_sales.values,
    color=["skyblue", "orange", "green"]
)

plt.title(
    "Sales by Category",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Category",
    fontsize=12
)

plt.ylabel("Total Sales($)", fontsize =12)
plt.grid(axis="y", linestyle="--", alpha=0.5)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )
plt.tight_layout()
screenshot_path = BASE_DIR / "screenshots" / "sales_by_category.png"

plt.savefig(screenshot_path, dpi=300)

print("Chart saved successfully!")
plt.show()

profit_region = df.groupby("Region")["Profit"].sum()
plt.figure(figsize=(8,5))
bars = plt.bar(
    profit_region.index,
    profit_region.values,
    color=["skyblue", "orange", "green", "red"]
)

plt.title(
    "Profit By Region",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel(
    "Region",
    fontsize=12
)

plt.ylabel("Net Profit($)", fontsize =12)
plt.grid(axis="y", linestyle="--", alpha=0.5)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )
plt.tight_layout()
screenshot_path = BASE_DIR / "screenshots" / "profit_by_region.png"

plt.savefig(screenshot_path, dpi=300)

print("Profit chart saved!")
plt.show()


top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
plt.figure(figsize=(10,6))

bars = plt.barh(
    top_customers.index,
    top_customers.values,
    color="steelblue"
)

plt.title(
    "Top 10 Customers by Sales",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Total Sales ($)",
    fontsize=12
)

plt.ylabel(
    "Customer",
    fontsize=12
)

plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.gca().invert_yaxis()
plt.tight_layout()
screenshot_path = BASE_DIR / "screenshots" / "most_valuable_customers.png"

plt.savefig(screenshot_path, dpi=300)

print("Valuable Customers chart saved!")
plt.show()  

plt.hist(df["Sales"])
plt.figure(figsize=(10, 6))

plt.hist(
    df["Sales"],
    bins=30,
    edgecolor="black"
)

plt.title(
    "Distribution of Sales",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Sales ($)",
    fontsize=12
)

plt.ylabel(
    "Number of Orders",
    fontsize=12
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
screenshot_path = BASE_DIR / "screenshots" / "sales_distribution.png"

plt.savefig(screenshot_path, dpi=300)

print("Sales Distribution chart saved!")

plt.show()

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5,
    s=15
)

plt.title(
    "Discount vs Profit",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Discount",
    fontsize=12
)

plt.ylabel(
    "Profit ($)",
    fontsize=12
)

plt.grid(
    linestyle="--",
    alpha=0.5
)
plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    linewidth=1
)
plt.tight_layout()

screenshot_path = BASE_DIR / "screenshots" / "discount_vs_profit.png"

plt.savefig(screenshot_path, dpi=300)

print("Discount vs Profit chart saved!")

plt.show()
