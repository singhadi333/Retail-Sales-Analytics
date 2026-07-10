import pandas as pd
from faker import Faker
import random

fake = Faker("en_IN")

customers = []

for customer_id in range(1, 100001):
    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number()[:15],
        "address": fake.address().replace("\n", ", "),
        "city": fake.city(),
        "join_date": fake.date_between(start_date="-5y", end_date="today")
    })

df = pd.DataFrame(customers)

df.to_csv(
    "data\\generated\\customers.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())
print(f"\nGenerated {len(df)} customers successfully!")