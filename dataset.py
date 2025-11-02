import pandas as pd
import random
import numpy as np

data = {
    "order_id": range(1001, 1011),
    "customer_name": ["Rahul", "Priya", "Karan", "Asha", "Vikram"] * 2,
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"] * 2,
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Audio"] * 2,
    "price": [55000, 500, 800, 12000, 2000, np.nan, 800, 12000, np.nan, 55000],
    "quantity": [1, 5, 3, 2, np.nan, 4, 3, 1, 2, 1],
    "order_date": pd.date_range(start="2024-01-01", periods=10, freq="M")
}

df = pd.DataFrame(data)
df.to_csv("datasets.csv", index=False)
print("✅ datasets.csv created successfully!")
