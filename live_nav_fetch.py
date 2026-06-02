import pandas as pd
import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/live_nav_125497.csv", index=False)

print(df.head())
print("NAV data saved successfully")
import pandas as pd
import requests

amfi_codes = [119551, 120503, 118632, 119092, 120841]

for code in amfi_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(f"data/raw/nav_{code}.csv", index=False)

    print(f"NAV data saved for {code}")