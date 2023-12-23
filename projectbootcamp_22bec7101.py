import pandas as pd

# Create a DataFrame from the provided data
data = {
    'Beverage_category': ['Coffee'] * 4 + ['Classic Espresso Drinks'] * 73,
    'Beverage': ['Brewed Coffee'] * 4 + ['Caffè Latte'] * 15 + ['Caffè Mocha (Without Whipped Cream)'] * 15 + ['Vanilla Latte (Or Other Flavoured Latte)'] * 15 + ['Caffè Americano'] * 4 + ['Cappuccino'] * 15 + ['Espresso'] * 2 + ['Skinny Latte (Any Flavour)'] * 1,
    'Beverage_prep': ['Short', 'Tall', 'Grande', 'Venti'] * 21,
    'Calories': [3, 4, 5, 5] + [70, 100, 70, 100, 150, 110, 130, 170, 200, 180, 220, 260, 230, 280, 340, 290] * 3 + [60],
    'Total Fat (g)': [0.1, 0.1, 0.1, 0.1] + [0.1, 3.5, 2.5, 0.2, 6, 4.5, 0.3, 7, 5, 0.3, 9, 7, 0.4, 9, 0.1] * 3 + [0.1],
    'Trans Fat (g)': [0, 0, 0, 0] + [0.1, 0, 0.4, 0.2, 3.5, 1.5, 1.5, 2, 4.5, 0.2, 6, 2, 1.5, 2, 0.1] * 3 + [0.1],
    'Saturated Fat (g)': [0, 0, 0, 0] + [0, 0.1, 0, 0.2, 0.2, 0.5, 0.2, 3.5, 1.5, 0.2, 4.5, 1, 1.5, 0.2, 0.1] * 3 + [0.1],
    'Sodium (mg)': [0, 0, 0, 0] + [5, 15, 0, 5, 25, 0, 5, 30, 0, 10, 35, 0, 5, 25, 0, 10, 30] * 3 + [5],
    'Total Carbohydrates (g)': [5, 10, 10, 10] + [75, 85, 65, 120, 135, 105, 150, 170, 130, 190, 220, 170, 160, 190, 240, 180] * 3 + [80],
    'Cholesterol (mg)': [0, 0, 0, 0] + [10, 10, 6, 15, 15, 10, 19, 19, 13, 25, 24, 16, 21, 21, 19, 32, 28] * 3 + [9]
}

df = pd.DataFrame(data)

# View separate columns
print(df.columns)

# View the first 5 rows
print(df.head())

# Drop a column (e.g., 'Trans Fat (g)')
df = df.drop('Trans Fat (g)', axis=1)

# View unique values in 'Beverage_category'
print(df['Beverage_category'].unique())
import matplotlib.pyplot as plt

# Bar plot for Calories
plt.figure(figsize=(10, 6))
plt.bar(df['Beverage_prep'], df['Calories'], color='skyblue')
plt.xlabel('Beverage Preparation')
plt.ylabel('Calories')
plt.title('Calories in Different Beverage Preparations')
plt.xticks(rotation=45, ha='right')
plt.show()

# Line plot for Calories
plt.figure(figsize=(10, 6))
plt.plot(df['Beverage_prep'], df['Calories'], marker='o', color='orange', linestyle='--', linewidth=2)
plt.xlabel('Beverage Preparation')
plt.ylabel('Calories')
plt.title('Calories in Different Beverage Preparations')
plt.xticks(rotation=45, ha='right')
plt.show()
