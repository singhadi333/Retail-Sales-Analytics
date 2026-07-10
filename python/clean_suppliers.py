import pandas as pd
import re

# Read raw dataset
df = pd.read_csv("data/raw/suppliers.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing supplier names
# -----------------------------
df["supplier_name"] = df["supplier_name"].fillna("Unknown Supplier")

# -----------------------------
# Fill missing contact person
# -----------------------------
df["contact_person"] = df["contact_person"].fillna("Unknown")

# -----------------------------
# Fill missing phone numbers
# -----------------------------
df["phone"] = df["phone"].fillna("Not Available")

# -----------------------------
# Remove extra spaces
# -----------------------------
df["supplier_name"] = df["supplier_name"].str.strip()
df["contact_person"] = df["contact_person"].str.strip()

# -----------------------------
# Standardize text
# -----------------------------
df["supplier_name"] = df["supplier_name"].str.title()
df["contact_person"] = df["contact_person"].str.title()

# -----------------------------
# Remove invalid emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# -----------------------------
# Fix missing/invalid emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_mask = ~df["email"].fillna("").str.match(email_pattern)

df.loc[invalid_mask, "email"] = [
    f"unknown_supplier_{i}@shopsmart.com"
    for i in df.index[invalid_mask]
]

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/suppliers.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Suppliers cleaned successfully!")