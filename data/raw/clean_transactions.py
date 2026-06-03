import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Print column names
print("Columns in file:")
print(df.columns.tolist())

# Standardize transaction type
if "transaction_type" in df.columns:
    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

# Standardize KYC status
if "kyc_status" in df.columns:
    df["kyc_status"] = (
        df["kyc_status"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

# Remove duplicates
df = df.drop_duplicates()

# Find amount column automatically
amount_col = None

for col in df.columns:
    if "amount" in col.lower():
        amount_col = col
        break

if amount_col:
    df = df[df[amount_col] > 0]
    print(f"Using amount column: {amount_col}")
else:
    print("Amount column not found!")

# Valid transaction types
if "transaction_type" in df.columns:
    valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]
    df = df[df["transaction_type"].isin(valid_types)]

# Valid KYC statuses
if "kyc_status" in df.columns:
    valid_kyc = ["VERIFIED", "PENDING"]
    df = df[df["kyc_status"].isin(valid_kyc)]

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Investor transactions cleaned successfully!")
print("Total rows:", len(df))