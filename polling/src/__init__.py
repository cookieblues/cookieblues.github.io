import pickle

import pandas as pd
import pystan

from config import *


def jackman2005(party_name):
    df = pd.read_csv(DATA_DIRECTORY / "raw/polls.csv")
    party_code = PARTIES[party_name]

    # Create date column
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])
    df = df.sort_values(by="date", ascending=True)
    df.index = df["date"]
    df = df.drop(["year", "month", "day", "date"], axis=1)

    # Drop nans
    df = df.loc[~df[party_code].isnull()].copy()

    # Go from last election
    df = df.loc[df.index > PREV_ELECTION_DATES[0]].copy()
    df["time"] = (df.index-pd.Timestamp(PREV_ELECTION_DATES[0])).days

    # Factorize pollsters
    pollsters, uniq_pollsters = pd.factorize(df["pollingfirm"])
    df["pollingfirm"] = pollsters

    # Impute missing sample sizes
    df["n"] = df["n"].fillna(1000)

    # Calculate standard error
    df[f"{party_code}_se"] = (df[party_code]) * (100-(df[party_code])) / df["n"]
    # Add a little bit to values that are 0
    df.loc[df[f"{party_code}_se"] == 0, f"{party_code}_se"] = 1e-100

    # Prepare data for stan
    model_data = {
        "N": df.shape[0],
        "T": (pd.Timestamp.today()-pd.Timestamp(PREV_ELECTION_DATES[0])).days+2,
        "y": df[party_code],
        "s": df[f"{party_code}_se"],
        "time": df["time"]+1,
        "H": len(uniq_pollsters),
        "house": pollsters+1,
        "alpha_init": PREV_ELECTION_RESULTS[party_name],
        #"alpha_final": 30.0,
        "delta_loc": 0,
        "zeta_scale": 5,
        "tau_scale": 3
    }
    
    # Compile model
    model_filepath = MODEL_DIRECTORY / "jackman2005.pkl"
    if model_filepath.exists():
        model = pickle.load(open(model_filepath, "rb"))
    else:
        model = pystan.StanModel(model_code=JACKMAN_2005)
        with open(model_filepath, "wb") as outfile:
            pickle.dump(model, outfile)

    # Sample from model
    posterior = model.sampling(data=model_data, chains=4, iter=1000, seed=1)
    posterior_df = pd.DataFrame()
    posterior_df["alpha"] = posterior["alpha"].mean(axis=0)
    posterior_df["omega"] = posterior["omega"].mean(axis=0)
    return posterior_df

