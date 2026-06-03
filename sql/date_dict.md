# Data Dictionary

## fact_nav

amfi_code : Mutual fund identifier

date : NAV date

nav : Net Asset Value of the fund

---

## fact_transactions

investor_id : Unique investor identifier

transaction_date : Date of transaction

amfi_code : Mutual fund code

transaction_type : SIP / Lumpsum / Redemption

amount_inr : Transaction amount in INR

state : Investor state

city : Investor city

city_tier : Tier classification of city

age_group : Investor age category

gender : Investor gender

annual_income_lakh : Annual income in lakhs

payment_mode : Payment method used

kyc_status : VERIFIED or PENDING

---

## fact_performance

amfi_code : Mutual fund identifier

scheme_name : Name of mutual fund scheme

fund_house : Fund management company

category : Fund category

return_1yr_pct : One-year return percentage

return_3yr_pct : Three-year return percentage

return_5yr_pct : Five-year return percentage

benchmark_3yr_pct : Benchmark return percentage

alpha : Risk-adjusted excess return

beta : Market sensitivity measure

sharpe_ratio : Risk-adjusted performance measure

sortino_ratio : Downside-risk adjusted return

std_dev_ann_pct : Annualized standard deviation

max_drawdown_pct : Maximum decline from peak value

aum_crore : Assets under management (crores)

expense_ratio_pct : Fund expense ratio

morningstar_rating : Morningstar rating

risk_grade : Fund risk category