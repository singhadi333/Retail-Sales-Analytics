import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

positions = [
    "Store Manager",
    "Sales Executive",
    "Cashier",
    "Inventory Executive"
]

employees = []

for employee_id in range(1, 401):
    employees.append({
        "employee_id": employee_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number()[:15],
        "store_id": random.randint(1, 10),
        "position": random.choice(positions),
        "salary": random.randint(18000, 80000),
        "joining_date": fake.date_between(start_date="-8y", end_date="today")
    })

df = pd.DataFrame(employees)

df.to_csv(
    "data\\generated\\employees.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())