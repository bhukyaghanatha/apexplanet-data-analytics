# ApexPlanet Data Analytics Internship
## Final Project Report

**Project:** E-Commerce Sales Data Analytics  
**Internship:** ApexPlanet Software Pvt. Ltd.

---

# Table of Contents

1. Executive Summary
2. Problem Statement
3. Objectives
4. Data Source and Overview
5. Technology Stack
6. Methodology
7. Exploratory Data Analysis
8. Key Findings
9. Statistical Analysis
10. Machine Learning Results
11. Dashboard
12. Business Recommendations
13. Limitations
14. Future Scope
15. Conclusion

---

# 1. Executive Summary

This project analyzes an e-commerce sales dataset to identify sales trends,
customer behavior, product performance, regional patterns, and business
opportunities.

The project covers data cleaning, exploratory data analysis, SQL-based data
extraction, visualization, dashboard development, statistical analysis, and
machine learning.

The final outcome is an interactive Power BI dashboard together with Python
analysis notebooks, SQL queries, cleaned data, and automation scripts.

---

# 2. Problem Statement

E-commerce businesses generate large amounts of sales and customer data.
Without proper analysis, it can be difficult to identify important trends,
understand customer behavior, monitor returns, and make data-driven business
decisions.

The objective of this project is to transform raw e-commerce data into useful
business insights.

---

# 3. Objectives

- Clean and prepare the raw dataset.
- Analyze sales and customer-related patterns.
- Perform SQL-based data extraction.
- Create meaningful visualizations.
- Develop an interactive Power BI dashboard.
- Perform statistical analysis.
- Build and evaluate machine learning models.
- Generate actionable business recommendations.
- Automate the analytics workflow.

---

# 4. Data Source and Overview

The project uses an e-commerce sales dataset containing information about:

- Orders
- Customers
- Products
- Categories
- Prices
- Discounts
- Quantities
- Payment methods
- Order dates
- Delivery time
- Regions
- Returns
- Sales amount
- Shipping costs
- Profit margins
- Customer age
- Customer gender

## Dataset Size

**Rows:** 4,851  
**Columns:** 17

---

# 5. Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- SQL
- Power BI
- Jupyter Notebook
- Git & GitHub

---

# 6. Methodology

The project followed these major stages:

1. Data collection
2. Data cleaning
3. Data preprocessing
4. Exploratory Data Analysis
5. SQL analysis
6. Data visualization
7. Power BI dashboard development
8. Statistical analysis
9. Machine learning
10. Business recommendations
11. Automation
12. Final reporting

---

# 7. Exploratory Data Analysis

The cleaned dataset was analyzed to understand:

- Sales trends over time
- Sales by category
- Sales by region
- Payment methods
- Return patterns
- Customer demographics
- Product pricing
- Quantity purchased
- Profit-related patterns

Visualizations were created using Python and Power BI.

---

# 8. Key Findings

### Finding 1 — Sales Performance

The cleaned dataset contains 4,851 records and 17 variables. The average order value (total_amount) is 116.77, while the median is 58.35. The distribution is positively skewed, indicating that a smaller number of higher-value orders contribute to the overall sales value.

### Finding 2 — Category Performance

Monthly sales varied throughout the analyzed period. The highest monthly sales recorded in the dataset were 28,217.66 in May 2025, while the lowest were 9,317.49 in September 2025. Monthly sales analysis helps identify periods of stronger and weaker sales performance.

### Finding 3 — Regional Performance

Out of 4,851 orders, 4,602 orders were not returned and 249 orders were returned. This shows that returned orders represent a smaller portion of the overall dataset.

### Finding 4 — Returns

A Welch's independent t-test was performed to compare sales amounts between returned and non-returned orders. The test produced a p-value of 0.000342, indicating a statistically significant difference in sales amounts between the two groups.

### Finding 5 — Customer Behavior

A chi-square test was used to examine the relationship between product category and return status. The test produced a chi-square statistic of 56.18 and a p-value of approximately 2.67 × 10⁻¹⁰, indicating a statistically significant association between category and returns.

### Finding 6 — Payment Methods

A one-way ANOVA was performed to compare total sales across product categories. The test produced an F-statistic of 790.12 with a p-value effectively equal to zero, indicating a statistically significant difference in sales among the categories.

### Finding 7 — Profitability

Correlation analysis showed a strong positive relationship between price and total sales amount, with a correlation coefficient of 0.916. Profit margin also showed a strong positive relationship with total sales amount, with a correlation coefficient of 0.897. Quantity had a weaker positive relationship with total sales amount (0.273), while delivery time and customer age showed very weak relationships with sales.

---

# 9. Statistical Analysis

Statistical analysis was performed to understand the distribution of the numerical variables and identify significant relationships in the e-commerce dataset.

### Descriptive Statistics

The average total sales amount per order was 116.77, with a median of 58.35. The average price was 91.30, while the average profit margin was 21.77. The average delivery time was approximately 4.81 days.

### Confidence Interval

The estimated mean total sales amount was 116.77. The 95% confidence interval for the population mean was approximately 113.16 to 120.38.

### T-Test: Sales and Returns

A Welch's independent t-test was conducted to compare total sales amounts between returned and non-returned orders.

* **t-statistic:** -3.627
* **p-value:** 0.000342

Since the p-value is below 0.05, there is a statistically significant difference in total sales amounts between returned and non-returned orders.

### Chi-Square Test: Category and Returns

A chi-square test of independence was performed to examine the relationship between product category and return status.

* **Chi-square statistic:** 56.185
* **p-value:** 2.67 × 10⁻¹⁰

The result indicates a statistically significant association between product category and return status.

### ANOVA: Sales Across Categories

A one-way ANOVA was performed to determine whether total sales amounts differed across product categories.

* **F-statistic:** 790.121
* **p-value:** approximately 0

The result indicates that total sales amounts differ significantly across the product categories.

### Correlation Analysis

Correlation analysis identified the following relationships with total sales amount:

* Price and total amount: **0.916**
* Profit margin and total amount: **0.897**
* Shipping cost and total amount: **0.817**
* Quantity and total amount: **0.273**
* Delivery time and total amount: **-0.013**
* Customer age and total amount: **-0.013**

The strongest positive relationships with total sales amount were observed for price and profit margin.


# 10. Machine Learning Results

Machine learning models were developed to perform both classification and numerical prediction using the cleaned e-commerce dataset.

### Classification Models

Two classification models were implemented to predict whether an order would be returned:

* Logistic Regression
* Decision Tree Classifier

Both models achieved an accuracy of approximately **94.9%**. However, both models recorded **0.0 precision, 0.0 recall, and 0.0 F1-score** for the returned (`Yes`) class. This indicates that the models did not successfully identify returned orders in the test data.

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |    0.949 |     0.000 |  0.000 |    0.000 |
| Decision Tree       |    0.949 |     0.000 |  0.000 |    0.000 |

The Logistic Regression model produced a **ROC-AUC score of 0.603**, indicating limited ability to distinguish between returned and non-returned orders.

The classification results should therefore be interpreted carefully. The high accuracy is influenced by the imbalance between returned and non-returned orders, and accuracy alone does not indicate good return prediction performance.

### Regression Model

A Linear Regression model was developed to predict `total_amount`.

The model achieved the following results:

* **R² Score:** 0.956
* **MAE:** 18.02
* **RMSE:** 27.05

The R² score of 0.956 indicates that the model explains a large proportion of the variation in total order amount within the test data. The MAE and RMSE provide measures of the prediction error.

### Feature Importance

The Decision Tree feature-importance analysis identified several variables with higher predictive importance, including shipping cost and selected encoded customer, product, and order identifiers. These results should be treated as predictive relationships rather than evidence of direct causation.

### Model Limitation

The classification models were not effective at identifying returned orders because the returned class was much smaller than the non-returned class. Future work should address this class imbalance using techniques such as class weighting, resampling, or more suitable evaluation strategies.

# 11. Dashboard

An interactive Power BI dashboard was developed to provide a clear visual overview of the e-commerce business performance.

The dashboard was created using the cleaned e-commerce dataset and includes key business metrics, trends, category-level analysis, regional analysis, return analysis, and profit analysis.

### Dashboard Components

The dashboard includes:

* **Total Sales:** 566.45K
* **Total Orders:** 4,851
* **Total Customers:** approximately 3.58K
* **Monthly Sales Trend**
* **Sales by Category**
* **Sales by Region**
* **Returns Analysis**
* **Profit by Category**
* **Interactive filters for Category, Region, Payment Method, and Date**

The dashboard allows users to filter the data and interactively explore different aspects of business performance.

### Dashboard File

The Power BI dashboard is available in the project repository:

`dashboards/ecommerce_dashboards.pbix`

The dashboard provides a consolidated view of sales performance and supports business decision-making through interactive visual analysis.

# 12. Business Recommendations

# 12. Business Recommendations

Based on the exploratory analysis, statistical tests, dashboard findings, and machine learning results, the following recommendations can be made:

### 1. Focus on High-Value Products

Price showed a strong positive relationship with total sales amount. The business can focus on high-value products while maintaining competitive pricing and suitable promotional strategies.

### 2. Monitor Product Categories

The analysis found a statistically significant relationship between product category and return status. Categories with relatively higher return activity should be monitored to identify possible product, quality, or customer-experience issues.

### 3. Improve Return Management

Returned orders represented a smaller portion of the overall dataset, but return-related differences were statistically significant. The business should track return reasons and category-level return patterns to reduce avoidable returns.

### 4. Use Sales Trends for Planning

Monthly sales showed noticeable variation, with May 2025 recording the highest monthly sales in the analyzed period. Businesses can use historical sales trends to improve inventory planning, promotions, and resource allocation.

### 5. Monitor Profitability

Profit margin showed a strong positive relationship with total sales amount. Sales growth should therefore be evaluated together with profitability rather than using sales volume alone.

### 6. Improve Return Prediction Models

The current classification models did not successfully identify returned orders. Future models should address class imbalance and use additional return-related features to improve the detection of potentially returned orders.

### 7. Use Customer Segmentation

The analysis produced five customer clusters based on recency, frequency, monetary value, and quantity. These segments can support targeted marketing strategies and differentiated customer engagement.

Overall, the combination of dashboard reporting, statistical analysis, customer segmentation, and predictive modeling can help the business make more informed and data-driven decisions.

# 13. Limitations

The project has several limitations that should be considered when interpreting the results:

1. **Dataset Size and Scope**
   The analysis was performed on the available e-commerce dataset and may not represent the complete business environment.

2. **Class Imbalance**
   Returned orders were much fewer than non-returned orders. This affected the performance of the classification models and resulted in poor identification of returned orders.

3. **High-Cardinality Identifiers**
   Some predictive features included customer, product, and order identifiers. These variables can introduce noise or dataset-specific patterns and should be handled carefully in future modeling.

4. **Limited Historical Information**
   The dataset covers a specific period, so longer-term changes in customer behavior and market conditions may not be fully represented.

5. **Forecasting Limitations**
   The time-series forecast is based on historical sales patterns and may not account for unexpected business events, seasonal changes, promotions, or external factors.

6. **Model Limitations**
   The machine learning models used in this project are basic predictive models. More advanced algorithms and feature engineering could potentially improve prediction performance.

7. **Business Context**
   Statistical relationships identified in the analysis should not automat


# 14. Future Scope

The project can be further improved and extended in the following areas:

1. **Advanced Machine Learning Models**
   More advanced classification and regression algorithms can be tested to improve prediction performance.

2. **Better Handling of Class Imbalance**
   Techniques such as class weighting, resampling, and other imbalance-handling methods can be applied to improve returned-order prediction.

3. **Improved Feature Engineering**
   Customer behavior, product characteristics, purchase frequency, and other meaningful business features can be engineered to improve model performance.

4. **Real-Time Analytics**
   The project can be extended to process real-time sales and customer data so that dashboards and KPIs can be updated automatically.

5. **Automated Dashboard Refresh**
   The analytics pipeline can be connected to scheduled data refresh processes to reduce manual work.

6. **Advanced Customer Segmentation**
   Future work can compare different clustering techniques and use additional customer behavior features to create more detailed customer segments.

7. **Deployment as a Business Application**
   The models and analytics pipeline could be deployed as a web-based application or cloud service for easier access by business users.

8. **External Data Integration**
   Future analysis could incorporate additional information such as marketing campaigns, seasonal events, customer feedback, and product reviews to provide deeper business insights.

# 15. Conclusion

This project provided a complete data analytics workflow for an e-commerce dataset, covering data cleaning, exploratory data analysis, SQL-based analysis, interactive dashboard development, statistical analysis, customer segmentation, time-series forecasting, and machine learning.

The analysis identified important patterns in sales, returns, product categories, regions, profitability, and customer behavior. Statistical testing helped determine which observed relationships were statistically significant, while machine learning models demonstrated both the potential and limitations of predictive analytics on the available data.

The Power BI dashboard provides an interactive way to monitor key business metrics and explore sales performance. The project also highlighted the importance of handling class imbalance, selecting meaningful features, and interpreting machine learning results carefully.

Overall, the project demonstrates how Python, SQL, Power BI, statistics, and machine learning can be combined to transform raw e-commerce data into useful business insights and support data-driven decision-making.


# Table of Contents

1. Executive Summary
2. Problem Statement
3. Objectives
4. Data Source and Overview
5. Technology Stack
6. Methodology
7. Exploratory Data Analysis
8. Key Findings
9. Statistical Analysis
10. Machine Learning Results
11. Dashboard
12. Business Recommendations
13. Limitations
14. Future Scope
15. Conclusion
