import pandas as pd
import numpy as np
import re

# -----------------------------
# Load Raw Dataset
# -----------------------------
df = pd.read_csv("data/raw/customers.csv")

print("=" * 50)
print("CUSTOMERS DATA CLEANING")
print("=" * 50)

print("\nDataset Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -----------------------------
# Remove Extra Spaces
# -----------------------------
df["first_name"] = df["first_name"].str.strip()
df["last_name"] = df["last_name"].str.strip()

# -----------------------------
# Standardize Names
# -----------------------------
df["first_name"] = df["first_name"].str.title()
df["last_name"] = df["last_name"].str.title()

# -----------------------------
# Fix Missing Cities
# -----------------------------
df["city"] = df["city"].fillna("Unknown")

# -----------------------------
# Fix Missing Phone Numbers
# -----------------------------
df["phone"] = df["phone"].fillna("Not Available")

# -----------------------------
# Remove Invalid Emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

df.loc[
    ~df["email"].fillna("").str.match(email_pattern),
    "email"
] = np.nan

# -----------------------------
# Fill Missing Emails
# -----------------------------
df["email"] = df["email"].fillna("unknown@email.com")

# -----------------------------
# Convert Join Date
# -----------------------------
df["join_date"] = pd.to_datetime(df["join_date"])

# -----------------------------
# Remove Future Dates
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["join_date"] > today, "join_date"] = today

# -----------------------------
# Remove Duplicate Customers
# -----------------------------
df = df.drop_duplicates(subset="customer_id")

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv(
    "data/cleaned/customers.csv",
    index=False,
    encoding="utf-8"
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:", df.shape)

print("\nCleaned dataset saved successfully!")