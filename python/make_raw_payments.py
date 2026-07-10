import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/payments.csv")

# ---------------------------------
# 1. Missing Payment Method (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "payment_method"] = None

# ---------------------------------
# 2. Missing Payment Status (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=2).index
df.loc[rows, "payment_status"] = None

# ---------------------------------
# 3. Negative Payment Amount (0.5%)
# ---------------------------------
rows = df.sample(frac=0.005, random_state=3).index
df.loc[rows, "amount"] *= -1

# ---------------------------------
# 4. Duplicate Transaction IDs (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=4).index
df.loc[rows, "transaction_id"] = "DUPLICATE_TXN"

# ---------------------------------
# 5. Future Payment Dates (0.5%)
# ---------------------------------
df["payment_date"] = pd.to_datetime(df["payment_date"])

rows = df.sample(frac=0.005, random_state=5).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "payment_date"] = future_dates

# ---------------------------------
# 6. Duplicate Records (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=6)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/payments.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Payments Dataset Created Successfully!")
print(df.shape)