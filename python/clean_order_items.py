import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/order_items.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing discount
# -----------------------------
df["discount"] = df["discount"].fillna(0)

# -----------------------------
# Fix negative quantity
# -----------------------------
df.loc[df["quantity"] <= 0, "quantity"] = 1

# -----------------------------
# Fix negative unit price
# -----------------------------
df["unit_price"] = df["unit_price"].abs()

# -----------------------------
# Round discount
# -----------------------------
df["discount"] = df["discount"].round(2)

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/order_items.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Order Items cleaned successfully!")