import pandas as pd

categories = [
    "Electronics",
    "Mobile Phones",
    "Computers",
    "Home Appliances",
    "Furniture",
    "Kitchen & Dining",
    "Fashion",
    "Footwear",
    "Beauty & Personal Care",
    "Health & Wellness",
    "Sports & Fitness",
    "Books",
    "Toys & Games",
    "Baby Products",
    "Groceries",
    "Beverages",
    "Stationery",
    "Jewelry",
    "Watches",
    "Automotive",
    "Pet Supplies",
    "Garden & Outdoor",
    "Office Supplies",
    "Musical Instruments",
    "Travel Accessories"
]

category_ids = range(1, len(categories) + 1)

df = pd.DataFrame({
    "category_id": category_ids,
    "category_name": categories
})

df.to_csv("data\\generated\\categories.csv", index=False, encoding="utf-8")

print("Categories generated successfully!")
print(df)