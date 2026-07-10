import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/orders.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate orders
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing order status
# -----------------------------
df["order_status"] = df["order_status"].fillna("Pending")

# -----------------------------
# Fill missing shipping address
# -----------------------------
df["shipping_address"] = df["shipping_address"].fillna("Address Not Available")

# -----------------------------
# Convert order_date to datetime
# -----------------------------
df["order_date"] = pd.to_datetime(df["order_date"])

# -----------------------------
# Replace future dates with today's date
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["order_date"] > today, "order_date"] = today

# -----------------------------
# Fix negative total amount
# -----------------------------
df["total_amount"] = df["total_amount"].abs()

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/orders.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Orders cleaned successfully!")