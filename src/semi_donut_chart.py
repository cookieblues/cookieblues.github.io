import altair as alt
import numpy as np
import pandas as pd

from constants import PARTIES
from utils import calculate_mandates

FOLKETINGET_SORTING = [
    "Socialdemokratiet",
    "Enhedslisten",
    "Socialistisk Folkeparti",
    "Alternativet",
    "Veganerpartiet",
    "Radikale Venstre",
    "Moderaterne",
    "Liberal Alliance",
    "Kristendemokraterne",
    "Dansk Folkeparti",
    "Borgernes Parti",
    "Nye Borgerlige",
    "Danmarksdemokraterne",
    "Stram Kurs",
    "Venstre",
    "Det Konservative Folkeparti",
]

# prepare data
# df1 = pd.read_csv("data/current_popularity_dist.csv")
df = pd.read_csv("data/latent_party_probs.csv", parse_dates=["date"])
df = df.loc[df["date"] >= pd.Timestamp.now() - pd.Timedelta(days=365)]
df = df.dropna(axis=1, how="all")

parties = df.columns.difference(["date", "other"])
df = calculate_mandates(df[parties])
latest_estimation = df.iloc[-1][df.iloc[-1] > 0]
df = latest_estimation.reset_index()  # only use latest estimation and disregard 0s
df.columns = ["party", "value"]
df["party_letter"] = df["party"].map(lambda party: PARTIES[party]["letter"])

# reorder according to left-right
df["party"] = pd.Categorical(df["party"], categories=FOLKETINGET_SORTING, ordered=True)
df = df.sort_values("party").reset_index(drop=True)

# base chart
RADIUS = 400
base = (
    alt.Chart(df)
    .transform_calculate(
        order=f"indexof({FOLKETINGET_SORTING}, datum.party)"  # get the order
    )
    .mark_arc(
        outerRadius=RADIUS,
        innerRadius=RADIUS / 5,
        opacity=0.75,
        stroke="white",
        strokeWidth=2,
    )
    .encode(
        theta=alt.Theta(
            field="value",
            type="quantitative",
            stack=True,
            scale=alt.Scale(type="linear", rangeMax=(np.pi / 2), rangeMin=-(np.pi / 2)),
            sort=None,
        ),
        order=alt.Order(field="order", type="quantitative", sort="ascending"),
        color=alt.Color(
            field="party",
            type="nominal",
            scale=alt.Scale(
                domain=FOLKETINGET_SORTING,
                range=[PARTIES[p]["color"] for p in FOLKETINGET_SORTING],
            ),
            legend=None,
            sort=FOLKETINGET_SORTING,
        ),
    )
)

party_letters = base.mark_text(
    radius=RADIUS * 1.06,
    size=RADIUS / 10,
    fontWeight="bold",
    stroke="#aeaeae",
    strokeWidth=1,
).encode(text="party_letter:N")
n_mandates = base.mark_text(
    radius=RADIUS / 2 + RADIUS / 10,
    size=RADIUS / 10,
    fontWeight="bold",
    stroke="#aeaeae",
    strokeWidth=1.25,
).encode(text="value:Q")

# Combine all layers
chart = alt.layer(base, party_letters, n_mandates)
chart.properties(
    width="container",
    height=10,
).save("js/semi_donut_chart.json")
