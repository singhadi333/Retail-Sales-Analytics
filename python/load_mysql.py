import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# -----------------------------
# MySQL Connection
# -----------------------------
connection_url = URL.create(
    drivername="mysql+mysqlconnector",
    username="root",
    password="MySQL@1234",      # Change if required
    host="localhost",
    port=3306,
    database="shopsmart"
)

engine = create_engine(connection_url)

# -----------------------------
# Loading Order
# -----------------------------
tables = [
    "categories",
    "suppliers",
    "stores",
    "products",
    "customers",
    "employees",
    "orders",
    "order_items",
    "payments",
    "returns"
]

print("=" * 50)
print("Loading Data into MySQL")
print("=" * 50)

for table in tables:

    print(f"\nLoading {table}...")

    df = pd.read_csv(f"data/cleaned/{table}.csv")

    df.to_sql(
        name=table,
        con=engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=5000
    )

    print(f"✅ {len(df):,} rows inserted")

print("\n🎉 All datasets loaded successfully!")