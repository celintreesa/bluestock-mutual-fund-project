import pandas as pd

# Read NAV history file
df_nav = pd.read_csv("data/raw/02_nav_history.csv")

# Check data
print(df_nav.head())
print(df_nav.columns)
print(df_nav.info())
import pandas as pd


df_nav = pd.read_csv("data/raw/02_nav_history.csv")

df_nav["date"] = pd.to_datetime(df_nav["date"])

df_nav = df_nav.sort_values(
    by=["amfi_code", "date"]
)

# Forward-fill missing NAV values
df_nav["nav"] = (
    df_nav.groupby("amfi_code")["nav"]
    .ffill()
)

df_nav = df_nav.drop_duplicates()

df_nav = df_nav[df_nav["nav"] > 0]

df_nav.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("NAV history cleaned successfully!")