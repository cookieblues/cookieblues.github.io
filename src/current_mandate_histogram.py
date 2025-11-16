from itertools import batched

import altair as alt
import numpy as np
import pandas as pd

from utils import calculate_mandates
from constants import PARTIES


N_SIMS = 500
WIDTH = 275
df = pd.read_csv("data/current_popularity_dist.csv")

df[df < 0.0005] = np.nan
df = df.dropna(how="all", axis=1)
df = df.fillna(0)
df = calculate_mandates(df)
medians = df.median().sort_values(ascending=False)
parties = medians.index

chart_columns = list()
charts = list()
for party in parties:
    hist_df = df[party].value_counts().reset_index()
    hist_df["Probability"] = 100 * hist_df["count"] / N_SIMS
    xmin = max(0-0.5, df[party].min()-2)
    xmax = int(df[party].max()+5) if medians.loc[party] < 4 else int(df[party].max()+3)
    bins = range(int(xmin), xmax)
    chart = alt.Chart(hist_df).mark_bar(
        size=0.85*WIDTH/len(bins),
        color=PARTIES[party]["color"],
        stroke="#aeaeae",
        strokeWidth=1,
    ).encode(
        x=alt.X(
            party,
            type="quantitative",
            scale=alt.Scale(bins=bins, domain=[xmin, xmax]),
        ),
        y="Probability"
    ).properties(
        width=WIDTH,
        height=WIDTH*0.675,
    )
    charts.append(chart)

chart_rows = [alt.hconcat(*row) for row in batched(charts, 3)]
chart = alt.vconcat(*chart_rows)

chart.save("js/current_mandate_histogram.json")
