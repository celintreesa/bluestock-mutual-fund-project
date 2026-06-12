import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Categories:")
print(df["risk_category"].unique())

