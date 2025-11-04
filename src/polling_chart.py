import altair as alt
import pandas as pd

PARTY_COLORS = {
    "Socialdemokratiet": "#C10B20",
    "Radikale Venstre": "#D50080",
    "Det Konservative Folkeparti": "#034536",
    "Nye Borgerlige": "#024450",
    "Klaus Riskær Pedersen": "#1F9FAC",
    "Socialistisk Folkeparti": "#A40000",
    "Veganerpartiet": "#80A51A",
    "Liberal Alliance": "#0A1B3E",
    "Kristendemokraterne": "#F5820B",
    "Dansk Folkeparti": "#FFFF00",
    "Stram Kurs": "#000000",
    "Venstre": "#003460",
    "Enhedslisten": "#D0004D",
    "Alternativet": "#00FF00"
}

# prepare data
df = pd.read_csv("polling/data/processed/mean_polls.csv")
df["date"] = pd.to_datetime(df["date"])
parties = [col for col in df.columns if col != "date" and col != "other"]
chart_data = df.melt(id_vars=["date"], value_vars=parties, var_name="party", value_name="value")

# base chart
base = alt.Chart(chart_data).encode(
    x=alt.X("date", title="Date"),
    y=alt.Y("value:Q", title="Polling percentage")
)

# nearest date selection for vertical ruler
nearest_date = alt.selection_point(
    nearest=True, 
    on="pointerover", 
    fields=["date"],
    empty=False
)

# nearest party selection for line highlight
nearest_party = alt.selection_point(
    nearest=True,
    on="pointerover",
    fields=["party"],
)

# neares party selection when clicking
click_selection = alt.selection_point(
    nearest=True,
    on="click",
    fields=["party"],
    toggle="true",  # enables toggling of parties without holding shift
)

nearest_points = base.mark_circle().encode(
    opacity=alt.value(0),
).add_params(nearest_date, nearest_party, click_selection)

# party lines
lines = base.mark_line().encode(
    color=alt.Color(
        "party:N",
        scale=alt.Scale(domain=list(PARTY_COLORS.keys()), range=list(PARTY_COLORS.values())),
        legend=None,
    ),
    size=alt.condition(nearest_party | click_selection, alt.value(3), alt.value(0.1))
).add_params(nearest_party, click_selection)

# dynamic label text
formatted = base.transform_calculate(
    formatted_text="datum['party'] + ' ' + format(datum['value'], '.1f') + '%'"
)
text = formatted.mark_text(
    align="left",
    dx=1,
    dy=-10,
    fontSize=16,
    fontWeight="bold",
    stroke="#cecece",
    strokeWidth=1,
).encode(
    text=alt.when(nearest_date).then("formatted_text:N").otherwise(alt.value(" ")),
    color=alt.Color(
        "party:N",
        scale=alt.Scale(domain=list(PARTY_COLORS.keys()), range=list(PARTY_COLORS.values())),
        legend=None,
    ),
    opacity=alt.condition(nearest_party | click_selection, alt.value(1), alt.value(0.05)),
)

# vertical rule for current date
rules = base.mark_rule(color="gray").encode(x="date").transform_filter(nearest_date)

# Combine all layers
chart = alt.layer(nearest_points, lines, text, rules)
chart.properties(
    width="container",
    height=600,
).configure(
    padding={"right": 280}  # increase value until labels are visible
).save("js/polling_chart.json")
