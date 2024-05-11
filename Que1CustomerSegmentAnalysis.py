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

# Group data by Customer Segment and aggregate total sales and profit
segment_summary = df.groupby('Customer Segment').agg({'Total Sales': 'sum', 'Cost per Unit': 'sum'}).reset_index()
segment_summary.rename(columns={'Cost per Unit': 'Total Cost'}, inplace=True)

# Calculate Profit for each customer segment
segment_summary['Profit'] = segment_summary['Total Sales'] - segment_summary['Total Cost']

# Calculate Profit Margin for each customer segment (in percentage)
segment_summary['Profit Margin (%)'] = (segment_summary['Profit'] / segment_summary['Total Sales']) * 100

# Define the desired sequence of customer segments
desired_sequence = ['CS1', 'CS2', 'CS3']  # Customize this list based on your specific sequence

# Filter and reorder customer segments based on the desired sequence
segment_summary_sorted = segment_summary.set_index('Customer Segment').loc[desired_sequence].reset_index()

# If there are additional customer segments not in the desired sequence, append them to the end
additional_segments = sorted(set(segment_summary['Customer Segment']) - set(desired_sequence))
segment_summary_sorted = pd.concat([
    segment_summary_sorted,
    segment_summary[segment_summary['Customer Segment'].isin(additional_segments)]
])

# Visualize Customer Segment Profitability Metrics in the desired sequence
plt.figure(figsize=(12, 8))

# Bar plot for Total Profit by Customer Segment
plt.subplot(2, 1, 1)
sns.barplot(x='Customer Segment', y='Profit', data=segment_summary_sorted, palette='coolwarm')
plt.title('Profit by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Profit')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Bar plot for Profit Margin by Customer Segment
plt.subplot(2, 1, 2)
sns.barplot(x='Customer Segment', y='Profit Margin (%)', data=segment_summary_sorted, palette='viridis')
plt.title('Profit Margin by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Profit Margin (%)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Adjust layout and display plots
plt.tight_layout()
plt.show()
