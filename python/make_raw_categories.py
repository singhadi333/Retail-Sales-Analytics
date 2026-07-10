import pandas as pd
import random

random.seed(42)

# Read clean dataset
df = pd.read_csv("data/generated/categories.csv")

# ---------------------------------
# 1. Missing Category Names (5%)
# ---------------------------------
rows = df.sample(frac=0.05, random_state=1).index
df.loc[rows, "category_name"] = None

# ---------------------------------
# 2. Extra Spaces in Category Names (10%)
# ---------------------------------
rows = df.sample(frac=0.10, random_state=2).index
df.loc[rows, "category_name"] = (
    " " + df.loc[rows, "category_name"].fillna("") + " "
)

# ---------------------------------
# 3. Convert Some Names to Uppercase (10%)
# ---------------------------------
rows = df.sample(frac=0.10, random_state=3).index
df.loc[rows, "category_name"] = (
    df.loc[rows, "category_name"].str.upper()
)

# ---------------------------------
# 4. Duplicate Records (10%)
# ---------------------------------
duplicates = df.sample(frac=0.10, random_state=4)
df = pd.concat([df, duplicates], ignore_index=True)

# Save Raw Dataset
df.to_csv(
    "data/raw/categories.csv",
    index=False,
    encoding="utf-8"
)

print("Raw Categories Dataset Created Successfully!")
print(df.shape)