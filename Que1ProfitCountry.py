import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def format_thousands(x, pos):
    return '$%1.0fK' % (x * 1e-3)

# Load the dataset (replace 'path_to_your_data.csv' with the path to your CSV file)
file_path = 'Case_Study_Business Analytics.xlsx - Data Set.csv'
df = pd.read_csv(file_path)

# Convert 'Cost per Unit' and 'Units Sold' columns to numeric data types
df['Cost per Unit'] = pd.to_numeric(df['Cost per Unit'], errors='coerce')
df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')

# Drop rows with NaN values (if needed)
df.dropna(subset=['Cost per Unit', 'Units Sold'], inplace=True)

# Calculate Total Sales for each transaction
df['Total Sales'] = df['Cost per Unit'] * df['Units Sold']

# Group data by Country and aggregate total sales and total cost
country_summary = df.groupby('Country').agg({'Total Sales': 'sum', 'Cost per Unit': 'sum'}).reset_index()
country_summary.rename(columns={'Cost per Unit': 'Total Cost'}, inplace=True)

# Calculate Profit for each country
country_summary['Profit'] = country_summary['Total Sales'] - country_summary['Total Cost']

# Sort countries by Profit (descending order)
country_summary_sorted = country_summary.sort_values(by='Profit', ascending=False)

# Print the top countries by profit
print("Top Countries by Profit:")
print(country_summary_sorted.head())

unique_countries = df['Country'].nunique()

# Print the total number of unique countries
print("Total number of countries:", unique_countries)

# Visualize the data using seaborn barplot with customized styling
plt.figure(figsize=(12, 8))
sns.barplot(x='Country', y='Profit', data=country_summary_sorted.head(10), palette='viridis')

# Annotate bars with profit values
for index, row in country_summary_sorted.head(10).iterrows():
    plt.text(index, row['Profit'], '$%.1fK' % (row['Profit'] * 1e-3), ha='center', va='bottom', fontsize=10, color='black')

# Format y-axis labels to display amounts in thousands of dollars
formatter = ticker.FuncFormatter(format_thousands)
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Top 10 Countries by Profit', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Profit (in $1,000)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
