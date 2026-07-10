import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

returns = []

RETURN_REASONS = [
    "Damaged Product",
    "Wrong Product Delivered",
    "Defective Item",
    "Customer Changed Mind",
    "Size Issue"
]

RETURN_STATUS = [
    "Approved",
    "Refunded",
    "Rejected"
]

# Generate 20,000 returns
for return_id in range(1, 20001):

    returns.append({
        "return_id": return_id,
        "order_item_id": random.randint(1, 750000),
        "return_date": fake.date_time_between(start_date="-2y", end_date="now"),
        "return_reason": random.choice(RETURN_REASONS),
        "refund_amount": round(random.uniform(100, 50000), 2),
        "return_status": random.choice(RETURN_STATUS)
    })

df = pd.DataFrame(returns)

df.to_csv(
    "data\\generated\\returns.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())
print(f"\nTotal Returns: {len(df)}")