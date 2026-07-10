import pandas as pd
import re

# -----------------------------
# Read Raw Dataset
# -----------------------------
df = pd.read_csv("data/raw/customers.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove Exact Duplicate Rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill Missing Values
# -----------------------------
df["first_name"] = df["first_name"].fillna("Unknown")
df["last_name"] = df["last_name"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["phone"] = df["phone"].fillna("Not Available")

# -----------------------------
# Remove Extra Spaces
# -----------------------------
df["first_name"] = df["first_name"].astype(str).str.strip()
df["last_name"] = df["last_name"].astype(str).str.strip()
df["city"] = df["city"].astype(str).str.strip()

# -----------------------------
# Standardize Text
# -----------------------------
df["first_name"] = df["first_name"].str.title()
df["last_name"] = df["last_name"].str.title()
df["city"] = df["city"].str.title()

# -----------------------------
# Fix Missing / Invalid Emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_mask = ~df["email"].fillna("").str.match(email_pattern)

df.loc[invalid_mask, "email"] = [
    f"unknown_customer_{i}@shopsmart.com"
    for i in df.index[invalid_mask]
]

# -----------------------------
# Make ALL Emails Unique
# -----------------------------
duplicate_mask = df["email"].duplicated(keep=False)

for idx in df[duplicate_mask].index:
    email = df.at[idx, "email"]

    if "@" in email:
        local, domain = email.split("@", 1)
        df.at[idx, "email"] = f"{local}_{df.at[idx,'customer_id']}@{domain}"
    else:
        df.at[idx, "email"] = f"unknown_customer_{df.at[idx,'customer_id']}@shopsmart.com"

# -----------------------------
# Convert Join Date
# -----------------------------
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

# Replace invalid dates
df["join_date"] = df["join_date"].fillna(pd.Timestamp("2024-01-01"))

# Replace future dates
today = pd.Timestamp.today()

df.loc[df["join_date"] > today, "join_date"] = today

# -----------------------------
# Validation
# -----------------------------
assert df["customer_id"].is_unique, "Duplicate Customer IDs found!"
assert df["email"].is_unique, "Duplicate emails still exist!"
assert df["first_name"].isnull().sum() == 0
assert df["last_name"].isnull().sum() == 0
assert df["email"].isnull().sum() == 0

print("\nValidation Passed ✓")

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Emails:", df["email"].duplicated().sum())

print("\nShape After:", df.shape)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv(
    "data/cleaned/customers.csv",
    index=False,
    encoding="utf-8"
)

print("\nCustomers cleaned successfully!")