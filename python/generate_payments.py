import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash",
    "Wallet"
]

payment_statuses = [
    "Success",
    "Success",
    "Success",
    "Success",
    "Failed",
    "Refunded"
]

payments = []

for payment_id in range(1, 250001):
    payments.append({
        "payment_id": payment_id,
        "order_id": payment_id,
        "amount": round(random.uniform(500, 100000), 2),
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choice(payment_statuses),
        "payment_date": fake.date_time_between(start_date="-2y", end_date="now"),
        "transaction_id": fake.uuid4()
    })

df = pd.DataFrame(payments)

df.to_csv(
    "data\\generated\\payments.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())
print(f"\nTotal Payments: {len(df)}")