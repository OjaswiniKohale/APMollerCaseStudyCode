import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_percentage_error

# Load the data from CSV file
data = pd.read_csv("Case_Study_Business Analytics.xlsx - Data Set.csv")

# Pre-processing: Drop any rows with missing or inconsistent data
data.dropna(inplace=True)

# Clean 'Cost per Unit' column by removing commas and converting to numeric
data['Cost per Unit'] = pd.to_numeric(data['Cost per Unit'].str.replace(',', ''), errors='coerce')

# Clean 'Units Sold' column by removing commas and converting to numeric
data['Units Sold'] = pd.to_numeric(data['Units Sold'].str.replace(',', ''), errors='coerce')

# Clean 'Total Sales' column by removing commas and converting to numeric
data['Total Sales'] = pd.to_numeric(data['Total Sales'].str.replace(',', ''), errors='coerce')

# Drop rows with missing or inconsistent cost per unit, units sold, and total sales values
data.dropna(subset=['Cost per Unit', 'Units Sold', 'Total Sales'], inplace=True)

# Calculate Total Sales by Customer Segment
customer_segment_sales = data.groupby('Customer Segment')['Total Sales'].sum()

# Fit SARIMA model
order = (6, 0, 6)  # ARIMA order
seasonal_order = (1, 2, 1, 7)  # Seasonal order
model = SARIMAX(customer_segment_sales, order=order, seasonal_order=seasonal_order, exog=None)
model_fit = model.fit()

# Forecast future sales
future_customer_segments = np.array(['CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'CS8']).reshape(-1, 1)
future_sales = model_fit.forecast(steps=len(future_customer_segments))

# Calculate MAPE
actual_sales = np.array(customer_segment_sales)
mape = mean_absolute_percentage_error(actual_sales, future_sales)

# Print MAPE
print("Mean Absolute Percentage Error (MAPE):", mape)

# Plotting the before and after scenario
plt.figure(figsize=(12, 8))
plt.bar(customer_segment_sales.index, customer_segment_sales, color='skyblue', label='Before')
plt.bar(future_customer_segments.flatten(), future_sales, color='peachpuff', alpha=0.5, label='After (Forecast)')
plt.title('Customer Segment Preferences')
plt.xlabel('Customer Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
