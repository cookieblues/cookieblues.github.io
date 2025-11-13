import altair as alt
import numpy as np
import pandas as pd

from constants import PARTIES


PARTY_LETTERS = {
    "Socialdemokratiet": "S",
    "Radikale Venstre": "B",
    "Det Konservative Folkeparti": "K",
    "Nye Borgerlige": "D",
    "Klaus Riskær Pedersen": "E",
    "Socialistisk Folkeparti": "F",
    "Veganerpartiet": "G",
    "Liberal Alliance": "I",
    "Kristendemokraterne": "K",
    "Dansk Folkeparti": "O",
    "Stram Kurs": "P",
    "Venstre": "V",
    "Enhedslisten": "Ø",
    "Alternativet": "Å",
}
folketinget_sorting = [
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

def calculate_mandates(df: pd.DataFrame) -> pd.DataFrame:
    adjusted_percentage = df[parties].div(df[parties].sum(axis=1), axis=0)
    above_barrier = adjusted_percentage >= 0.02
    mandate_key = adjusted_percentage[above_barrier].sum(axis=1) / 175
    total_allowed_n_mandates = adjusted_percentage[above_barrier].div(mandate_key, axis=0)
    n_mandates = pd.DataFrame(np.floor(total_allowed_n_mandates))
    leftover_mandates = 175-n_mandates.sum(axis=1)
    mandate_residue = (total_allowed_n_mandates-n_mandates).rank(axis=1, method="first", ascending=False)
    additional_mandates = mandate_residue.le(leftover_mandates, axis=0)
    n_mandates = n_mandates.fillna(0)
    n_mandates += additional_mandates
    return n_mandates.astype(int)

# prepare data
# df = pd.read_csv("polling/data/processed/mean_polls.csv", parse_dates=["date"])
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
df["party"] = pd.Categorical(df["party"], categories=folketinget_sorting, ordered=True)
df = df.sort_values("party").reset_index(drop=True)

# base chart
RADIUS = 400
base = alt.Chart(df).transform_calculate(
  order=f"indexof({folketinget_sorting}, datum.party)"  # get the order 
).mark_arc(
    outerRadius=RADIUS,
    innerRadius=RADIUS/5,
    opacity=0.75,
    stroke="white",
    strokeWidth=2,
).encode(
    theta=alt.Theta(
        field="value",
        type="quantitative",
        stack=True,
        scale=alt.Scale(type="linear", rangeMax=(np.pi/2), rangeMin=-(np.pi/2)),
        sort=None,
    ),
    order=alt.Order(field="order", type="quantitative", sort="ascending"),
    color=alt.Color(
        field="party",
        type="nominal",
        scale=alt.Scale(domain=folketinget_sorting, range=[PARTIES[p]["color"] for p in folketinget_sorting]),
        legend=None,
        sort=folketinget_sorting,
    ),
)

party_letters = base.mark_text(
    radius=RADIUS*1.06,
    size=RADIUS/10,
    fontWeight="bold",
    stroke="#aeaeae",
    strokeWidth=1,
).encode(
    text="party_letter:N"
)
n_mandates = base.mark_text(
    radius=RADIUS/2+RADIUS/10,
    size=RADIUS/10,
    fontWeight="bold",
    stroke="#aeaeae",
    strokeWidth=1.25,
).encode(
    text="value:Q"
)

# Combine all layers
chart = alt.layer(base, party_letters, n_mandates)
chart.properties(
    width="container",
).save("js/semi_donut_chart.json")
