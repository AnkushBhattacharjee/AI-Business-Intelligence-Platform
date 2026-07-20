# AI Business Intelligence Platform

## About this Journal

This journal documents the development of the AI Business Intelligence Platform. It records the objective of each milestone, the concepts learned, the code used, observations made, and the decisions taken throughout the project.

---

# Milestone 1 - Reading and Understanding the Dataset

## Objective

Read the Superstore dataset into Python and inspect its basic structure.

## Why?

Before analyzing any dataset, we must verify that it has been loaded correctly and understand its structure.

## Functions Used

- `pd.read_csv()`
- `df.head()`
- `df.shape`
- `df.columns`
- `df.dtypes`

## What I Learned

- How to read a CSV file using Pandas.
- Why `encoding="latin1"` was required.
- Difference between methods and attributes.
- How to use `pathlib` for project file paths.

## Observations

- Dataset loaded successfully.
- Dataset contains 9,994 rows.
- Dataset contains 21 columns.

---

# Milestone 2 - Data Quality Analysis

## Objective

Inspect the dataset before cleaning it.

## Why?

Before modifying any dataset, it is important to determine whether it contains missing values, duplicate records, or incorrect data types.

## Functions Used

- `df.info()`
- `df.isnull().sum()`
- `df.duplicated().sum()`
- `df.describe()`

## What I Learned

(To be updated after our discussion.)

## Observations

- No missing values.
- No duplicate rows.
- Numeric columns contain valid business data.
- Dataset is ready for exploratory data analysis.

## Conclusion

No cleaning is required at this stage.

## Milestone 4 – Advanced Exploratory Data Analysis

### Objective
Learn advanced data analysis techniques using Pandas.

### Topics Covered
- Data Filtering
- Multiple GroupBy
- Aggregation (.agg())
- Pivot Tables

### What I Learned
- Filter rows based on conditions.
- Group data using multiple columns.
- Calculate multiple statistics using agg().
- Build pivot tables for business reporting.

### Conclusion
The project can now answer complex business questions and summarize data in a structured format.