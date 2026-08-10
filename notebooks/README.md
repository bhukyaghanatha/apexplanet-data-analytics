# ApexPlanet Task 1 - E-commerce Sales Data Analysis

## Project Overview

This project performs data cleaning, preprocessing, and exploratory data analysis (EDA) on an e-commerce sales dataset using Python.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset

The dataset contains e-commerce order information including:

- Order ID
- Customer ID
- Product ID
- Category
- Price
- Discount
- Quantity
- Payment Method
- Order Date
- Delivery Time
- Region
- Returned Status
- Total Amount
- Shipping Cost
- Profit Margin
- Customer Age
- Customer Gender

## Data Cleaning

The following preprocessing steps were performed:

1. Checked the dataset structure and data types.
2. Checked for missing values.
3. Checked for duplicate records.
4. Converted the order date to datetime format.
5. Identified potential outliers using the IQR method.
6. Applied IQR capping to continuous numerical variables.
7. Saved the cleaned dataset in `data/processed/`.

## Exploratory Data Analysis

The following analyses were performed:

- Statistical summary
- Value counts for categorical variables
- Histograms
- Boxplots
- Bar charts
- Scatter plots
- Correlation heatmap
- Pattern, trend, and anomaly identification

## Key Findings

- Most orders contain 1 or 2 units.
- Credit Card is the most frequently used payment method.
- Most orders were not returned.
- Price and total order amount show a positive relationship.
- Delivery time is mainly concentrated around 4–6 days.

## Project Structure

```text
apexplanet-data-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── scripts/
├── reports/
├── dashboards/
│
└── README.md
## Data Source

The dataset used for this project is an e-commerce sales dataset provided for the internship task. It contains order, customer, product, payment, delivery, return, and financial information.

## Limitations

- The dataset contains limited information about customer and product details.
- The dataset does not provide detailed information about marketing campaigns or customer behavior.
- Some extreme numerical values required outlier treatment using the IQR method.
- The analysis is limited to the variables available in the dataset.
