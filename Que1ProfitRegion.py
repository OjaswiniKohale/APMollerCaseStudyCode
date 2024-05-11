import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = {
    'Business Area': ['Africa'] * 11,
    'Country': ['Angola'] * 11,
    'Product Name': [
        'Household goods, personal effects, not for resale or public distribution',
        'Machinery or mechanical appliances, new per unit weight less than 2 tons',
        'Pastry, bread, cake, non-frozen, foodstuff',
        'White goods',
        'Batteries',
        'Pastry, bread, cake, non-frozen, foodstuff',
        'Tea, bags, non-frozen',
        'Adhesive tape, plastic',
        'Aluminium, aluminium articles, metal per unit weight less than 2 tons',
        'Chemical products, nos',
        'Garments, apparel, new'
    ],
    'Customer Segment': ['CS1'] * 11,
    'Industry Segment': ['Computers', 'Computers', 'Computers', 'Computers', 'Consumer Goods',
                         'Consumer Goods', 'Consumer Goods', 'Fashion Apparel', 'Fashion Apparel',
                         'Fashion Apparel', 'Fashion Apparel'],
    'Cost per Unit': [2961, 1169, 1255, 1718, 992, 1244, 1712, 562, 695, 814, 575],
    'Units Sold': [1, 2, 1, 14, 1, 1, 3, 34, 8, 2, 11],
    'Total Sales': [8984, 16572, 1688, 110974, 6166, 1707, 15563, 192855, 43556, 10175, 80512]
}

df = pd.DataFrame(data)

def calculate_profit_margin(cost, sales):
    return ((sales - cost) / sales) * 100

# Select three common products
common_products = ['White goods', 'Adhesive tape, plastic', 'Tea, bags, non-frozen']

# Compute profit margins for selected products
profit_margins = {}
for product in common_products:
    product_data = df[df['Product Name'] == product]
    total_cost = product_data['Cost per Unit'].sum()
    total_sales = product_data['Total Sales'].sum()
    margin = calculate_profit_margin(total_cost, total_sales)
    profit_margins[product] = margin

print(profit_margins)

# Prepare data for plotting
products = list(profit_margins.keys())
margins = list(profit_margins.values())

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(products, margins, marker='o', color='b')
plt.title('Profit Margins of Products in Angola')
plt.xlabel('Product')
plt.ylabel('Profit Margin (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
