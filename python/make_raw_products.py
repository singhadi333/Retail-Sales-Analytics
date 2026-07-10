import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/products.csv")

# ---------------------------------
# 1. Missing Brand (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "brand"] = None

# ---------------------------------
# 2. Missing Product Name (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=2).index
df.loc[rows, "product_name"] = None

# ---------------------------------
# 3. Negative Stock Quantity (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=3).index
df.loc[rows, "stock_quantity"] = -10

# ---------------------------------
# 4. Selling Price Less Than Cost Price (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=4).index
df.loc[rows, "selling_price"] = df.loc[rows, "cost_price"] * 0.8

# ---------------------------------
# 5. Extra Spaces in Product Name (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=5).index
df.loc[rows, "product_name"] = (
    " " + df.loc[rows, "product_name"].fillna("") + " "
)

# ---------------------------------
# 6. Duplicate Records (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=6)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/products.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Products Dataset Created Successfully!")
print(df.shape)