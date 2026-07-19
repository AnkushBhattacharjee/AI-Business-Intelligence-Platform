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