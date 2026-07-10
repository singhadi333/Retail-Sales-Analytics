import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/employees.csv")

# ---------------------------------
# 1. Missing Email (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "email"] = None

# ---------------------------------
# 2. Missing Phone (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=2).index
df.loc[rows, "phone"] = None

# ---------------------------------
# 3. Negative Salary (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=3).index
df.loc[rows, "salary"] *= -1

# ---------------------------------
# 4. Future Joining Dates (0.5%)
# ---------------------------------
df["joining_date"] = pd.to_datetime(df["joining_date"])

rows = df.sample(frac=0.005, random_state=4).index

future_dates = pd.date_range(
    start="2027-01-01",
    periods=len(rows),
    freq="D"
)

df.loc[rows, "joining_date"] = future_dates

# ---------------------------------
# 5. Extra Spaces in First Name (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=5).index
df.loc[rows, "first_name"] = (
    " " + df.loc[rows, "first_name"].fillna("") + " "
)

# ---------------------------------
# 6. Duplicate Records (1%)
# ---------------------------------
duplicates = df.sample(frac=0.01, random_state=6)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/employees.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Employees Dataset Created Successfully!")
print(df.shape)