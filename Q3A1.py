import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

# Load and preprocess your dataset (replace 'path_to_your_data.csv' with the actual file path)
file_path = 'Case_Study_Business Analytics.xlsx - Data Set.csv'
df = pd.read_csv(file_path)

# Convert 'Total Sales' column to numeric
df['Total Sales'] = pd.to_numeric(df['Total Sales'], errors='coerce')

# Drop rows with missing values in 'Total Sales' and 'Country' columns
df.dropna(subset=['Total Sales', 'Country'], inplace=True)

# Aggregate data by country to calculate total revenue
country_summary = df.groupby('Country')['Total Sales'].sum().reset_index()

# Filter countries with sufficient data points for forecasting (e.g., at least 12 months of data)
valid_countries = country_summary[country_summary['Total Sales'].notna() & (country_summary['Total Sales'].count() >= 12)]['Country']

# Select a subset of countries with adequate data for revenue forecasting
forecast_countries = valid_countries.head(5)  # Adjust the number of forecasted countries as needed

# Plot Current and Enhanced Forecasted Revenue for selected countries
plt.figure(figsize=(12, 8))

for country in forecast_countries:
    country_data = df[df['Country'] == country]['Total Sales']
    
    if len(country_data) >= 12:  # Minimum 12 months of data for forecasting
        # Moving Average (MA) Forecast
        ma_forecast = country_data.rolling(window=12).mean().iloc[-1]
        
        # Growth Assumption (e.g., 5% annual growth rate)
        growth_rate = 1.02
        forecast_values = [ma_forecast * (growth_rate ** i) for i in range(1, 13)]  # Forecasting next 12 months
        
        # Plot Current Revenue and Enhanced Forecasted Revenue
        plt.plot(range(len(country_data)), country_data.values, label=f'Current Revenue ({country})', marker='o', linestyle='-')
        plt.plot(range(len(country_data), len(country_data) + 12), forecast_values, label=f'Enhanced Forecasted Revenue ({country})', marker='o', linestyle='--')

plt.title('Current and Enhanced Forecasted Revenue by Country')
plt.xlabel('Months')
plt.ylabel('Total Sales ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
