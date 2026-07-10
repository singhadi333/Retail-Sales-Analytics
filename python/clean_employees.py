import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/employees.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing emails
# -----------------------------
df["email"] = df["email"].fillna("unknown@company.com")

# -----------------------------
# Fill missing phone numbers
# -----------------------------
df["phone"] = df["phone"].fillna("Not Available")

# -----------------------------
# Remove extra spaces
# -----------------------------
df["first_name"] = df["first_name"].str.strip()
df["last_name"] = df["last_name"].str.strip()

# -----------------------------
# Standardize names
# -----------------------------
df["first_name"] = df["first_name"].str.title()
df["last_name"] = df["last_name"].str.title()

# -----------------------------
# Fix negative salaries
# -----------------------------
df["salary"] = df["salary"].abs()

# -----------------------------
# Convert joining_date to datetime
# -----------------------------
df["joining_date"] = pd.to_datetime(df["joining_date"])

# -----------------------------
# Replace future joining dates
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["joining_date"] > today, "joining_date"] = today

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/employees.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Employees cleaned successfully!")