import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/stores.csv")

# ---------------------------------
# 1. Missing Contact Numbers (10%)
# ---------------------------------
rows = df.sample(frac=0.10, random_state=1).index
df.loc[rows, "contact_no"] = None

# ---------------------------------
# 2. Missing Store Names (5%)
# ---------------------------------
rows = df.sample(frac=0.05, random_state=2).index
df.loc[rows, "store_name"] = None

# ---------------------------------
# 3. Extra Spaces in Store Names (10%)
# ---------------------------------
rows = df.sample(frac=0.10, random_state=3).index
df.loc[rows, "store_name"] = (
    " " + df.loc[rows, "store_name"].fillna("") + " "
)

# ---------------------------------
# 4. Future Opening Dates (5%)
# ---------------------------------
df["opening_date"] = pd.to_datetime(df["opening_date"])

rows = df.sample(frac=0.05, random_state=4).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "opening_date"] = future_dates

# ---------------------------------
# 5. Duplicate Records (10%)
# ---------------------------------
duplicates = df.sample(frac=0.10, random_state=5)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/stores.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Stores Dataset Created Successfully!")
print(df.shape)