import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/suppliers.csv")

# ---------------------------------
# 1. Missing Contact Person (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=1).index
df.loc[rows, "contact_person"] = None

# ---------------------------------
# 2. Missing Email (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=2).index
df.loc[rows, "email"] = None

# ---------------------------------
# 3. Invalid Emails (1%)
# ---------------------------------
rows = df.sample(frac=0.01, random_state=3).index
df.loc[rows, "email"] = "invalid_email"

# ---------------------------------
# 4. Missing Phone Numbers (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=4).index
df.loc[rows, "phone"] = None

# ---------------------------------
# 5. Extra Spaces in Supplier Names (2%)
# ---------------------------------
rows = df.sample(frac=0.02, random_state=5).index
df.loc[rows, "supplier_name"] = (
    " " + df.loc[rows, "supplier_name"].fillna("") + " "
)

# ---------------------------------
# 6. Duplicate Records (2%)
# ---------------------------------
duplicates = df.sample(frac=0.02, random_state=6)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/suppliers.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Suppliers Dataset Created Successfully!")
print(df.shape)