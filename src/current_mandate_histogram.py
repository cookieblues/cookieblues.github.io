from itertools import batched

import altair as alt
import numpy as np
import pandas as pd

from utils import calculate_mandates
from constants import PARTIES


WIDTH = 275
df = pd.read_csv("data/current_popularity_dist.csv")
N_SIMS = len(df)

df[df < 0.0005] = np.nan
df = df.dropna(how="all", axis=1)
df = df.fillna(0)
df = calculate_mandates(df)
medians = df.agg(["median", "mean"]).T.sort_values(["median", "mean"], ascending=False)["median"]
parties = medians.index

chart_columns = list()
charts = list()
for party in parties:
    hist_df = df[party].value_counts().reset_index()
    hist_df["Probability"] = 100 * hist_df["count"] / N_SIMS
    xmin = max(0-0.5, df[party].min()-2)
    xmax = df[party].max()+4.5 if medians.loc[party] < 4 else df[party].max()+2.5
    bins = range(int(xmin), int(np.ceil(xmax)))
    chart = alt.Chart(
        hist_df
    ).mark_bar(
        size=0.85*WIDTH/len(bins),
        color=PARTIES[party]["color"],
        stroke="#aeaeae",
        strokeWidth=1,
    ).encode(
        x=alt.X(
            party,
            title=party,
            type="quantitative",
            scale=alt.Scale(bins=bins, domain=[xmin, xmax]),
        ),
        y=alt.Y("Probability", title="Probability [%]", ),
    ).properties(
        width=WIDTH,
        height=WIDTH*0.675,
    )
    charts.append(chart)

chart_rows = [alt.hconcat(*row) for row in batched(charts, 3)]
chart = alt.vconcat(*chart_rows).configure_axis(
    labelFontSize=10,
    titleFontSize=14,
)

chart.save("js/current_mandate_histogram.json")
chart.save("current_mandate_histogram.png")
