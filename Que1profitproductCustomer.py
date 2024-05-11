import pandas as pd
import matplotlib.pyplot as plt

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

# Group the data by Product Name and Customer Segment, and calculate total sales, total cost, and total units sold
profitability = data.groupby(['Product Name', 'Customer Segment']).agg({'Total Sales': 'sum', 'Cost per Unit': 'mean', 'Units Sold': 'sum'})

# Calculate profit by subtracting total cost from total sales
profitability['Profit'] = profitability['Total Sales'] - (profitability['Cost per Unit'] * profitability['Units Sold'])

# Sort the dataframe by profit in descending order
profitability = profitability.sort_values(by='Profit', ascending=False)

# Display the top 5 profitable product and customer segment combinations
top_profitable_combinations = profitability.head(5)

# Define colors for bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'orange', 'lightpink']

# Plotting the top profitable combinations with colorful bars
plt.figure(figsize=(12, 8))
top_profitable_combinations['Profit'].plot(kind='bar', color=colors)
plt.title('Top 5 Profitable Product and Customer Segment Combinations')
plt.xlabel('Product and Customer Segment')
plt.ylabel('Profit (Thousands $)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()