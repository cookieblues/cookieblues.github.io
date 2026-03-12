from itertools import batched

import altair as alt
import pandas as pd

from constants import PARTIES

# --- Config ---
WIDTH = 350
HEIGHT = 200

# --- Load & filter data ---
df = pd.read_csv("data/latent_party_probs.csv", parse_dates=["date"])
df = df.loc[df["date"] >= pd.Timestamp.now() - pd.Timedelta(days=365)]
df = df.dropna(axis=1, how="all")

# Detect parties (exclude date and "other")
parties_in_data = [col for col in df.columns if col not in ("date", "other")]

# Detect uncertainty columns: expects columns named like "party_lower" and "party_upper"
# Adjust the suffix naming below if your columns use a different convention
# e.g. "party_q05" / "party_q95", or "party_ci_low" / "party_ci_high"
LOWER_SUFFIX = "_lower"
UPPER_SUFFIX = "_upper"

parties_with_ci = [
    p for p in parties_in_data
    if f"{p}{LOWER_SUFFIX}" in df.columns and f"{p}{UPPER_SUFFIX}" in df.columns
]
parties_without_ci = [p for p in parties_in_data if p not in parties_with_ci]

# --- Shared selections ---
nearest_date = alt.selection_point(
    nearest=True,
    on="pointerover",
    fields=["date"],
    empty=False,
)

# --- Build one chart per party ---
charts = []
all_parties = list(PARTIES.keys())
colors = {p: PARTIES[p]["color"] for p in all_parties}

for party in all_parties:
    if party not in parties_in_data:
        continue

    color = colors.get(party, "#888888")

    # Columns for this party
    lower_col = f"{party}{LOWER_SUFFIX}"
    upper_col = f"{party}{UPPER_SUFFIX}"
    has_ci = lower_col in df.columns and upper_col in df.columns

    # Build per-party dataframe
    cols = ["date", party]
    if has_ci:
        cols += [lower_col, upper_col]
    party_df = df[cols].copy()
    party_df = party_df.rename(columns={
        party: "value",
        lower_col: "lower",
        upper_col: "upper",
    })

    base = alt.Chart(party_df).encode(
        x=alt.X("date:T", title="Date", axis=alt.Axis(format="%b %Y")),
    )

    # Confidence band
    if has_ci:
        band = base.mark_area(
            opacity=0.2,
            color=color,
            interpolate="monotone",
        ).encode(
            y=alt.Y("lower:Q", title="Support [%]"),
            y2=alt.Y2("upper:Q"),
        )

    # Centre line
    line = base.mark_line(
        color=color,
        strokeWidth=2,
        interpolate="monotone",
    ).encode(
        y=alt.Y("value:Q", title="Support [%]"),
    )

    # Vertical rule on hover
    rule_points = base.mark_circle(opacity=0).encode(
        y=alt.Y("value:Q"),
    ).add_params(nearest_date)

    rule = base.mark_rule(color="gray", strokeWidth=1).encode(
        x="date:T",
    ).transform_filter(nearest_date)

    # Tooltip dot
    dot = base.mark_circle(color=color, size=60).encode(
        y=alt.Y("value:Q"),
        opacity=alt.condition(nearest_date, alt.value(1), alt.value(0)),
        tooltip=[
            alt.Tooltip("date:T", title="Date", format="%d %b %Y"),
            alt.Tooltip("value:Q", title="Support (%)", format=".1f"),
            *(
                [
                    alt.Tooltip("lower:Q", title="Lower CI (%)", format=".1f"),
                    alt.Tooltip("upper:Q", title="Upper CI (%)", format=".1f"),
                ]
                if has_ci
                else []
            ),
        ],
    )

    layers = [rule_points, rule]
    if has_ci:
        layers.append(band)
    layers += [line, dot]

    chart = alt.layer(*layers).properties(
        width=WIDTH,
        height=HEIGHT,
        title=alt.TitleParams(
            text=party,
            color=color,
            fontSize=16,
            fontWeight="bold",
            anchor="start",
        ),
    )
    charts.append(chart)

# --- Arrange in rows of 3 ---
chart_rows = [alt.hconcat(*row).resolve_scale(y="independent") for row in batched(charts, 3)]
final_chart = alt.vconcat(*chart_rows).configure_axis(
    labelFontSize=10,
    titleFontSize=12,
).configure_view(
    stroke=None,
)

final_chart.save("js/polling_chart_multiples.json")
