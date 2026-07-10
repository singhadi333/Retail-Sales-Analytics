import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/orders.csv")

# ---------------------------------
# 1. Missing Shipping Address (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "shipping_address"] = None

# ---------------------------------
# 2. Missing Order Status (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=2).index
df.loc[rows, "order_status"] = None

# ---------------------------------
# 3. Negative Total Amount (0.5%)
# ---------------------------------
rows = df.sample(frac=0.005, random_state=3).index
df.loc[rows, "total_amount"] *= -1

# ---------------------------------
# 4. Future Order Dates (0.5%)
# ---------------------------------
df["order_date"] = pd.to_datetime(df["order_date"])

rows = df.sample(frac=0.005, random_state=4).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "order_date"] = future_dates

# ---------------------------------
# 5. Duplicate Orders (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=5)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/orders.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Orders Dataset Created Successfully!")
print(df.shape)