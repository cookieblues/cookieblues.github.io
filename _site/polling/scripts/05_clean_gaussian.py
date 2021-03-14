import pandas as pd

from config import *


polls = pd.read_csv("data/raw/polls.csv")
last_date = str(polls.iloc[-1]["year"]) + "-" + str(polls.iloc[-1]["month"]) + "-" + str(polls.iloc[-1]["day"])

df = pd.read_csv("data/processed/gaussian_posterior.csv")
vote_cols = list()

for col in df.columns:
    if "vote" in col:
        vote_cols.append(col)

df_new = df[vote_cols].mean(axis=0)
n_days = int(df_new.shape[0] / 15)
parties = sorted(PARTIES.keys()) + ["other"]
mean_df = pd.DataFrame(
    index=pd.date_range(end=pd.Timestamp(last_date), freq="D", periods=n_days),
    columns=parties
)

for party_idx in range(15):
    party = mean_df.columns[party_idx]
    mean_df[party] = df_new[n_days*party_idx:n_days*(party_idx+1)].values

mean_df.to_csv("data/processed/mean_polls_raw.csv", index=True, index_label="date")
breakpoint()


