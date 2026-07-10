import pandas as pd
from faker import Faker

fake = Faker("en_IN")

suppliers = []

for supplier_id in range(1, 201):
    suppliers.append({
        "supplier_id": supplier_id,
        "supplier_name": fake.company(),
        "contact_person": fake.name(),
        "email": fake.company_email(),
        "phone": fake.phone_number()[:15],
        "city": fake.city(),
        "state": fake.state()
    })

df = pd.DataFrame(suppliers)

df.to_csv("data\\generated\\suppliers.csv", index=False, encoding="utf-8")

print(df.head())