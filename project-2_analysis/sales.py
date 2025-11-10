import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor'],
    'price': [55000, 500, 800, 55000, 12000],
    'quantity': [2, 5, 3, None, 1],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics']
}

df = pd.DataFrame(data)
df.to_csv("ecommerce_sales.csv", index=False)
print("✅ ecommerce_sales.csv created successfully!")
