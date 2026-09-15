import pandas as pd
import logging

# Logging setup
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation script started")

# Input file
INPUT_FILE = "data/processed/ecommerce_sales_cleaned.csv"

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
# Data cleaning and transformation

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Check for missing values
missing_values = df.isnull().sum().sum()

print("Data cleaning completed!")
print("Missing values:", missing_values)
print("Rows after cleaning:", len(df))
# Calculate KPIs

total_sales = df["total_amount"].sum()
total_orders = len(df)
total_customers = df["customer_id"].nunique()
average_order_value = df["total_amount"].mean()
return_rate = (df["returned"] == "Yes").mean() * 100

print("\n--- KPI RESULTS ---")
print("Total Sales:", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))
print("Return Rate:", round(return_rate, 2), "%")
# Create KPI results table

results = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Return Rate"
    ],
    "Value": [
        total_sales,
        total_orders,
        total_customers,
        average_order_value,
        return_rate
    ]
})

# Export KPI results
OUTPUT_FILE = "data/processed/automation_results.csv"

results.to_csv(OUTPUT_FILE, index=False)

print("\nKPI results exported successfully!")
print("Saved to:", OUTPUT_FILE)
# Calculate monthly sales

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)

monthly_sales["order_date"] = monthly_sales["order_date"].astype(str)

print("\n--- MONTHLY SALES ---")
print(monthly_sales)
# Export monthly sales

MONTHLY_OUTPUT = "data/processed/monthly_sales.csv"

monthly_sales.to_csv(MONTHLY_OUTPUT, index=False)

print("\nMonthly sales exported successfully!")
print("Saved to:", MONTHLY_OUTPUT)
# Calculate sales by category

category_sales = (
    df.groupby("category")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)

print("\n--- SALES BY CATEGORY ---")
print(category_sales)
# Export category sales

CATEGORY_OUTPUT = "data/processed/category_sales.csv"

category_sales.to_csv(CATEGORY_OUTPUT, index=False)

print("\nCategory sales exported successfully!")
print("Saved to:", CATEGORY_OUTPUT)
