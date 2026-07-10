import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/products.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate products
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing product names
# -----------------------------
df["product_name"] = df["product_name"].fillna("Unknown Product")

# -----------------------------
# Fill missing brands
# -----------------------------
df["brand"] = df["brand"].fillna("Unknown")

# -----------------------------
# Remove extra spaces
# -----------------------------
df["product_name"] = df["product_name"].str.strip()
df["brand"] = df["brand"].str.strip()

# -----------------------------
# Standardize text
# -----------------------------
df["product_name"] = df["product_name"].str.title()
df["brand"] = df["brand"].str.title()

# -----------------------------
# Fix negative stock
# -----------------------------
df.loc[df["stock_quantity"] < 0, "stock_quantity"] = 0

# -----------------------------
# Fix selling price
# -----------------------------
mask = df["selling_price"] < df["cost_price"]

df.loc[mask, "selling_price"] = (
    df.loc[mask, "cost_price"] * 1.20
).round(2)

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/products.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)

print("Products cleaned successfully!")