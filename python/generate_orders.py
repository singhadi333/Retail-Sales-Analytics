import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

orders = []

statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Shipped",
    "Pending",
    "Cancelled"
]

for order_id in range(1, 250001):
    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, 100000),
        "store_id": random.randint(1, 10),
        "employee_id": random.randint(1, 400),
        "order_date": fake.date_time_between(start_date="-2y", end_date="now"),
        "order_status": random.choice(statuses),
        "shipping_address": fake.address().replace("\n", ", "),
        "total_amount": round(random.uniform(500, 100000), 2)
    })

df = pd.DataFrame(orders)

df.to_csv(
    "data\\generated\\orders.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())
print(f"\nTotal Orders: {len(df)}")