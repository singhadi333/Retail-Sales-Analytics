import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/payments.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing payment method
# -----------------------------
df["payment_method"] = df["payment_method"].fillna("Unknown")

# -----------------------------
# Fill missing payment status
# -----------------------------
df["payment_status"] = df["payment_status"].fillna("Pending")

# -----------------------------
# Fix negative payment amount
# -----------------------------
df["amount"] = df["amount"].abs()

# -----------------------------
# Convert payment_date to datetime
# -----------------------------
df["payment_date"] = pd.to_datetime(df["payment_date"])

# -----------------------------
# Replace future dates with today's date
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["payment_date"] > today, "payment_date"] = today

# -----------------------------
# Handle duplicate transaction IDs
# -----------------------------
duplicates = df["transaction_id"].duplicated()

df.loc[duplicates, "transaction_id"] = (
    df.loc[duplicates, "transaction_id"]
    + "_"
    + df.loc[duplicates].index.astype(str)
)

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/payments.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Payments cleaned successfully!")