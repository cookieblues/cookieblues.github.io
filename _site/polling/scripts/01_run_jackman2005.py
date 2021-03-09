import pandas as pd

from config import *
from src import jackman2005


idxs = pd.date_range(PREV_ELECTION_DATES[0], pd.Timestamp.today())
cols = list(PARTIES.keys())
df = pd.DataFrame(index=idxs, columns=cols)

for party_name in PARTIES.keys():
    print("="*20, party_name, "="*20)
    posterior_df = jackman2005(party_name)
    df[party_name] = posterior_df["alpha"].values

start_date = pd.Timestamp.today()-pd.DateOffset(months=6)
df = df.loc[df.index > start_date]
df.to_csv(DATA_DIRECTORY / "processed/mean_polls.csv", index_label="date")

