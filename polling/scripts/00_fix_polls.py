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

first_dates = dict()
last_dates = dict()

### Get poll data
new_df = df.copy()
new_df.columns = party_names

for party_name in party_names:
    first_dates[party_name] = new_df[~new_df[party_name].isnull()].index.min()
    last_dates[party_name] = new_df[~new_df[party_name].isnull()].index.max()

new_df = new_df.loc[
    start_date <= new_df.index,
    party_names
].copy()
new_df.to_csv("data/processed/fixed_polls.csv")

### Fix mean
mean_df = pd.read_csv("data/interim/mean_polls_raw.csv", index_col="date", parse_dates=["date"])
# Remove less than 0.05
#mean_df = mean_df[mean_df >= 0.05].copy()
mean_df = mean_df.loc[mean_df.index >= start_date].copy()

for party_name in party_names:
    # First date
    two_weeks_before_first_date = pd.date_range(first_dates[party_name] - pd.DateOffset(days=30), first_dates[party_name], freq="1D")
    for first_date in two_weeks_before_first_date:
        val = mean_df.loc[mean_df.index == first_date, party_name]
        if len(val) == 0:
            continue
        if val[0] < 0.14:
            continue
        else:
            break
    mean_df.loc[mean_df.index < first_date, party_name] = ""
    # Last date
    two_weeks_after_last_date = pd.date_range(last_dates[party_name], last_dates[party_name] + pd.DateOffset(days=30), freq="1D")
    for last_date in two_weeks_after_last_date:
        val = mean_df.loc[mean_df.index == last_date, party_name]
        if len(val) == 0:
            continue
        if val[0] < 0.14:
            break
    # if party_name == "Stram_Kurs":
    #     breakpoint()
    mean_df.loc[last_date < mean_df.index, party_name] = ""
mean_df.to_csv("data/processed/mean_polls.csv")

