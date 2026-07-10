import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/stores.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing store names
# -----------------------------
df["store_name"] = df["store_name"].fillna("Unknown Store")

# -----------------------------
# Fill missing contact numbers
# -----------------------------
df["contact_no"] = df["contact_no"].fillna("Not Available")

# -----------------------------
# Remove extra spaces
# -----------------------------
df["store_name"] = df["store_name"].str.strip()

# -----------------------------
# Standardize store names
# -----------------------------
df["store_name"] = df["store_name"].str.title()

# -----------------------------
# Convert opening_date to datetime
# -----------------------------
df["opening_date"] = pd.to_datetime(df["opening_date"])

# -----------------------------
# Replace future opening dates
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["opening_date"] > today, "opening_date"] = today

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/stores.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Stores cleaned successfully!")