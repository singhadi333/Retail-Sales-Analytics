import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/order_items.csv")

# ---------------------------------
# 1. Missing Discount (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "discount"] = None

# ---------------------------------
# 2. Negative Quantity (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=2).index
df.loc[rows, "quantity"] = -1

# ---------------------------------
# 3. Negative Unit Price (0.5%)
# ---------------------------------
rows = df.sample(frac=0.005, random_state=3).index
df.loc[rows, "unit_price"] *= -1

# ---------------------------------
# 4. Duplicate Records (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=4)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/order_items.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Order Items Dataset Created Successfully!")
print(df.shape)