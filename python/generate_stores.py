import pandas as pd
from faker import Faker

fake = Faker("en_IN")

store_names = [
    "Lucknow Hazratganj",
    "Noida Sector 18",
    "Delhi Connaught Place",
    "Gurugram Cyber City",
    "Mumbai Andheri",
    "Pune Hinjewadi",
    "Bengaluru MG Road",
    "Hyderabad Banjara Hills",
    "Chennai T Nagar",
    "Kolkata Park Street"
]

stores = []

for i, store_name in enumerate(store_names, start=1):
    stores.append({
        "store_id": i,
        "store_name": store_name,
        "city": fake.city(),
        "state": fake.state(),
        "contact_no": fake.phone_number()[:15],
        "opening_date": fake.date_between(start_date="-10y", end_date="today")
    })

df = pd.DataFrame(stores)

df.to_csv("data\\generated\\stores.csv", index=False, encoding="utf-8")

print(df)