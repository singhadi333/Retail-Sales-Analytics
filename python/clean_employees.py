import pandas as pd
import re

# -----------------------------
# Read Raw Dataset
# -----------------------------
df = pd.read_csv("data/raw/employees.csv")

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
df["phone"] = df["phone"].fillna("Not Available")
df["position"] = df["position"].fillna("Employee")

# -----------------------------
# Remove Extra Spaces
# -----------------------------
df["first_name"] = df["first_name"].astype(str).str.strip()
df["last_name"] = df["last_name"].astype(str).str.strip()
df["position"] = df["position"].astype(str).str.strip()

# -----------------------------
# Standardize Text
# -----------------------------
df["first_name"] = df["first_name"].str.title()
df["last_name"] = df["last_name"].str.title()
df["position"] = df["position"].str.title()

# -----------------------------
# Fix Missing / Invalid Emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_mask = ~df["email"].fillna("").str.match(email_pattern)

df.loc[invalid_mask, "email"] = [
    f"unknown_employee_{emp_id}@shopsmart.com"
    for emp_id in df.loc[invalid_mask, "employee_id"]
]

# -----------------------------
# Make ALL Emails Unique
# -----------------------------
duplicate_mask = df["email"].duplicated(keep=False)

for idx in df[duplicate_mask].index:

    email = df.at[idx, "email"]

    if "@" in email:
        local, domain = email.split("@", 1)
        df.at[idx, "email"] = (
            f"{local}_{df.at[idx,'employee_id']}@{domain}"
        )
    else:
        df.at[idx, "email"] = (
            f"unknown_employee_{df.at[idx,'employee_id']}@shopsmart.com"
        )

# -----------------------------
# Fix Joining Date
# -----------------------------
df["joining_date"] = pd.to_datetime(
    df["joining_date"],
    errors="coerce"
)

df["joining_date"] = df["joining_date"].fillna(
    pd.Timestamp("2024-01-01")
)

today = pd.Timestamp.today()

df.loc[
    df["joining_date"] > today,
    "joining_date"
] = today

# -----------------------------
# Salary Cleaning
# -----------------------------
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

median_salary = df["salary"].median()

df["salary"] = df["salary"].fillna(median_salary)

# -----------------------------
# Validation
# -----------------------------
assert df["employee_id"].is_unique, "Duplicate Employee IDs!"
assert df["email"].is_unique, "Duplicate Employee Emails!"
assert df["first_name"].isnull().sum() == 0
assert df["last_name"].isnull().sum() == 0
assert df["email"].isnull().sum() == 0
assert df["salary"].isnull().sum() == 0

print("\nValidation Passed ✓")

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Emails:", df["email"].duplicated().sum())

print("\nShape After:", df.shape)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv(
    "data/cleaned/employees.csv",
    index=False,
    encoding="utf-8"
)

print("\nEmployees cleaned successfully!")