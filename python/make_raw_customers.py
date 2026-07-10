import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/customers.csv")

# Convert data types
df["phone"] = df["phone"].astype("string")
df["email"] = df["email"].astype("string")
df["first_name"] = df["first_name"].astype("string")
df["last_name"] = df["last_name"].astype("string")
df["city"] = df["city"].astype("string")
df["join_date"] = pd.to_datetime(df["join_date"])

# --------------------------------------------------
# 1. Missing Emails (3%)
# --------------------------------------------------
rows = df.sample(frac=0.03, random_state=1).index
df.loc[rows, "email"] = pd.NA

# --------------------------------------------------
# 2. Missing Phone Numbers (2%)
# --------------------------------------------------
rows = df.sample(frac=0.02, random_state=2).index
df.loc[rows, "phone"] = pd.NA

# --------------------------------------------------
# 3. Missing Cities (2%)
# --------------------------------------------------
rows = df.sample(frac=0.02, random_state=3).index
df.loc[rows, "city"] = pd.NA

# --------------------------------------------------
# 4. Invalid Emails (1%)
# --------------------------------------------------
rows = df.sample(frac=0.01, random_state=4).index
df.loc[rows, "email"] = "invalid_email"

# --------------------------------------------------
# 5. Duplicate Phone Numbers (1%)
# --------------------------------------------------
rows = df.sample(frac=0.01, random_state=5).index
df.loc[rows, "phone"] = "9876543210"

# --------------------------------------------------
# 6. Extra Spaces in First Names (1%)
# --------------------------------------------------
rows = df.sample(frac=0.01, random_state=6).index
df.loc[rows, "first_name"] = (
    " " + df.loc[rows, "first_name"] + " "
)

# --------------------------------------------------
# 7. Uppercase Last Names (1%)
# --------------------------------------------------
rows = df.sample(frac=0.01, random_state=7).index
df.loc[rows, "last_name"] = (
    df.loc[rows, "last_name"].str.upper()
)

# --------------------------------------------------
# 8. Future Join Dates (0.5%)
# --------------------------------------------------
rows = df.sample(frac=0.005, random_state=8).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "join_date"] = future_dates

# Convert date back to YYYY-MM-DD format
df["join_date"] = df["join_date"].dt.strftime("%Y-%m-%d")

# Save raw dataset
df.to_csv(
    "data/raw/customers.csv",
    index=False,
    encoding="utf-8"
)

print("=" * 50)
print("Raw Customers Dataset Created Successfully!")
print("=" * 50)
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())