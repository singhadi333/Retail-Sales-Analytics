import random
import pandas as pd

order_items = []

order_item_id = 1

for order_id in range(1, 250001):

    # Each order contains 1 to 5 products
    number_of_items = random.randint(1, 5)

    for _ in range(number_of_items):

        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(100, 50000), 2)
        discount = round(random.uniform(0, 30), 2)

        order_items.append({
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": random.randint(1, 5000),
            "quantity": quantity,
            "unit_price": unit_price,
            "discount": discount
        })

        order_item_id += 1

df = pd.DataFrame(order_items)

df.to_csv(
    "data\\generated\\order_items.csv",
    index=False,
    encoding="utf-8"
)

print(df.head())
print(f"\nTotal Order Items: {len(df)}")