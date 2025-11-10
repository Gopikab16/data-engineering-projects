
import pandas as pd

df = pd.read_csv("datasets.csv")

print(df.info())
print(df.head())

df["price"].fillna(df["price"].mean(), inplace=True)
df["quantity"].fillna(1, inplace=True)

df.drop_duplicates(inplace=True)

df["total_sales"] = df["price"] * df["quantity"]

category_sales = df.groupby("category")["total_sales"].sum().reset_index()

df.to_csv("cleaned_sales.csv", index=False)
category_sales.to_csv("category_sales.csv", index=False)

print("✅ Cleaned data saved successfully!")
