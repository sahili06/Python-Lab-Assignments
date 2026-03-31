import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

months = data['month']

plt.figure(figsize=(8,5))
plt.plot(months, data['total_profit'], marker='o', linestyle='-', color='b')
plt.title('Total Profit per Month')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))

plt.plot(months, data['facecream'], label='Face Cream')
plt.plot(months, data['facewash'], label='Face Wash')
plt.plot(months, data['toothpaste'], label='Toothpaste')
plt.plot(months, data['bathingsoap'], label='Bathing Soap')
plt.plot(months, data['shampoo'], label='Shampoo')
plt.plot(months, data['moisturizer'], label='Moisturizer')

plt.title('Sales Data of All Products')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))

width = 0.3
plt.bar(months - width/2, data['facecream'], width=width, label='Face Cream')
plt.bar(months + width/2, data['facewash'], width=width, label='Face Wash')

plt.title('Face Cream and Face Wash Sales')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()

total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure(figsize=(8,8))
plt.pie(total_sales, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Total Sales Distribution of Products (Yearly)')
plt.show()
