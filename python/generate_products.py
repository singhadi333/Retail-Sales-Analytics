import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

brands = [
    "Samsung", "Apple", "Sony", "LG", "Dell",
    "HP", "Lenovo", "Boat", "Nike", "Adidas",
    "Puma", "Philips", "Canon", "Havells", "Godrej"
]

products = []

for product_id in range(1, 5001):
    cost_price = random.randint(100, 50000)
    selling_price = round(cost_price * random.uniform(1.10, 1.40), 2)

    products.append({
        "product_id": product_id,
        "product_name": fake.word().title() + " " + random.choice([
            "Pro", "Max", "Plus", "Lite", "Ultra"
        ]),
        "category_id": random.randint(1, 25),
        "supplier_id": random.randint(1, 200),
        "brand": random.choice(brands),
        "cost_price": cost_price,
        "selling_price": selling_price,
        "stock_quantity": random.randint(0, 500),
        "reorder_level": 10,
        "date_added": fake.date_between(start_date="-5y", end_date="today"),
        "is_active": random.choice([True, True, True, True, False])
    })

df = pd.DataFrame(products)

df.to_csv("data\\generated\\products.csv", index=False, encoding="utf-8")

print(df.head())