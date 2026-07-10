import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/returns.csv")

print("Shape Before:", df.shape)

# -----------------------------
# Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing return reason
# -----------------------------
df["return_reason"] = df["return_reason"].fillna("Not Specified")

# -----------------------------
# Fill missing return status
# -----------------------------
df["return_status"] = df["return_status"].fillna("Pending")

# -----------------------------
# Fix negative refund amounts
# -----------------------------
df["refund_amount"] = df["refund_amount"].abs()

# -----------------------------
# Convert return_date to datetime
# -----------------------------
df["return_date"] = pd.to_datetime(df["return_date"])

# -----------------------------
# Replace future dates with today's date
# -----------------------------
today = pd.Timestamp.today()

df.loc[df["return_date"] > today, "return_date"] = today

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/cleaned/returns.csv",
    index=False,
    encoding="utf-8"
)

print("Shape After:", df.shape)
print("Returns cleaned successfully!")