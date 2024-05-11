import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'path_to_your_data.csv' with the path to your CSV file)
file_path = 'Case_Study_Business Analytics.xlsx - Data Set.csv'
df = pd.read_csv(file_path)

# Convert 'Cost per Unit' and 'Units Sold' columns to numeric data types
df['Cost per Unit'] = pd.to_numeric(df['Cost per Unit'], errors='coerce')
df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')

# Calculate Total Sales for each transaction
df['Total Sales'] = df['Cost per Unit'] * df['Units Sold']

# Group data by Product Name and aggregate total sales and profit
product_summary = df.groupby('Product Name').agg({'Total Sales': 'sum', 'Cost per Unit': 'sum'}).reset_index()
product_summary.rename(columns={'Cost per Unit': 'Total Cost'}, inplace=True)

# Calculate Profit for each product
product_summary['Profit'] = product_summary['Total Sales'] - product_summary['Total Cost']

# Calculate Profit Margin for each product (in percentage)
product_summary['Profit Margin (%)'] = (product_summary['Profit'] / product_summary['Total Sales']) * 100

# Sort products by Total Sales (descending order) to identify top revenue-generating products
product_summary_sorted_by_sales = product_summary.sort_values(by='Total Sales', ascending=False)

# Filter to get top 5 products by Total Sales
top_products_by_sales = product_summary_sorted_by_sales.head(5)

# Sort products by Profit Margin (descending order) to identify high-margin products
product_summary_sorted_by_margin = product_summary.sort_values(by='Profit Margin (%)', ascending=False)

# Filter to get top 5 products by Profit Margin
top_products_by_margin = product_summary_sorted_by_margin.head(5)

# Extract first word from Product Name (assuming product names are separated by spaces)
top_products_by_sales['Product Name'] = top_products_by_sales['Product Name'].str.split().str[0]

# Visualize Product Revenue and Profit Metrics for top 5 products
plt.figure(figsize=(12, 8))

# Bar plot for Total Sales (Revenue) of top 5 products
plt.subplot(2, 1, 1)
sns.barplot(x='Product Name', y='Total Sales', data=top_products_by_sales, palette='coolwarm')
plt.title('Top 5 Products by Total Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')

# Bar plot for Profit Margin of top 5 products
plt.subplot(2, 1, 2)
sns.barplot(x='Product Name', y='Profit Margin (%)', data=top_products_by_margin, palette='viridis')
plt.title('Top 5 Products by Profit Margin')
plt.xlabel('Product Name')
plt.ylabel('Profit Margin (%)')

# Adjust layout and display plots
plt.tight_layout()
plt.show()
