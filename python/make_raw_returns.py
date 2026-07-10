import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/returns.csv")

# ---------------------------------
# 1. Missing Return Reason (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "return_reason"] = None

# ---------------------------------
# 2. Missing Return Status (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=2).index
df.loc[rows, "return_status"] = None

# ---------------------------------
# 3. Negative Refund Amount (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=3).index
df.loc[rows, "refund_amount"] *= -1

# ---------------------------------
# 4. Future Return Dates (0.5%)
# ---------------------------------
df["return_date"] = pd.to_datetime(df["return_date"])

rows = df.sample(frac=0.005, random_state=4).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "return_date"] = future_dates

# ---------------------------------
# 5. Duplicate Records (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=5)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/returns.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Returns Dataset Created Successfully!")
print(df.shape)