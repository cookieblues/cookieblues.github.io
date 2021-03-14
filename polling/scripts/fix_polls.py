import pandas as pd

party_names = [
    "Socialdemokratiet",
    "Radikale_Venstre",
    "Det_Konservative_Folkeparti",
    "Nye_Borgerlige",
    "Klaus_Riskær_Pedersen",
    "Socialistisk_Folkeparti",
    "Veganerpartiet",
    "Liberal_Alliance",
    "Kristendemokraterne",
    "Dansk_Folkeparti",
    "Stram_Kurs",
    "Venstre",
    "Enhedslisten",
    "Alternativet"
]

df = pd.read_csv("data/raw/polls.csv", usecols=[
    "year",
    "month",
    "day",
    "party_a",
    "party_b",
    "party_c",
    "party_d",
    "party_e",
    "party_f",
    "party_g",
    "party_i",
    "party_k",
    "party_o",
    "party_p",
    "party_v",
    "party_oe",
    "party_aa"
])

today = pd.to_datetime("today").date()
start_date = today-pd.DateOffset(months=12)
six_months_range = pd.date_range(start_date, today, freq="1D")

df["date"] = pd.to_datetime(df[["year", "month", "day"]])
df = df.sort_values(by="date", ascending=True)
df.index = df["date"]
df = df.drop(["year", "month", "day", "date"], axis=1)

### Fix mean
mean_df = pd.read_csv("data/processed/mean_polls_raw.csv", index_col="date", parse_dates=["date"])
# Remove less than 0.05
breakpoint()
#mean_df = mean_df[mean_df >= 0.05].copy()
mean_df = mean_df.loc[mean_df.index >= start_date].copy()
mean_df.to_csv("data/processed/mean_polls.csv")

### Get poll data
new_df = df.copy()
new_df.columns = party_names
new_df = new_df.loc[
    start_date <= new_df.index,
    party_names
].copy()
new_df.to_csv("data/processed/fixed_polls.csv")
