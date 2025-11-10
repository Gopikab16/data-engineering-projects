
import csv

with open("ecommerce_sales.csv", "r") as infile, open("cleaned_sales.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row["price"] == "":
            row["price"] = "0"   # fill missing price
        if row["quantity"] == "":
            row["quantity"] = "1"
        writer.writerow(row)

print("✅ Cleaned data saved to cleaned_sales.csv")
