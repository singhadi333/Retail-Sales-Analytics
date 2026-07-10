import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/categories.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing category names
# -----------------------------
df["category_name"] = df["category_name"].fillna("Unknown Category")

# -----------------------------
# Remove extra spaces
# -----------------------------
df["category_name"] = df["category_name"].str.strip()

# -----------------------------
# Standardize category names
# -----------------------------
df["category_name"] = df["category_name"].str.title()

# -----------------------------
# Remove duplicate category names
# -----------------------------
df = df.drop_duplicates(subset="category_name")

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/categories.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Categories cleaned successfully!")