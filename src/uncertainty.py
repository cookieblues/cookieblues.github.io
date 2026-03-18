import altair as alt
import numpy as np
import pandas as pd

from constants import PARTIES

# --- Config ---
WIDTH = 350
HEIGHT = 200

# --- Load & filter data ---
df = pd.read_csv("data/latent_party_probs_all.csv", parse_dates=["date"])
df = df.loc[df["date"] >= df["date"].max() - pd.Timedelta(days=30)]
df = df.dropna(axis=1, how="all")

# Detect uncertainty columns: expects columns named like "party_lower" and "party_upper"
# Adjust the suffix naming below if your columns use a different convention
# e.g. "party_q05" / "party_q95", or "party_ci_low" / "party_ci_high"
LOWER_SUFFIX = "_lower"
UPPER_SUFFIX = "_upper"

# Detect parties (exclude date and "other")
# parties_in_data = [col for col in df.columns if col not in ("date", "other")]
parties_in_data = [
    col
    for col in df.columns
    if col not in ("date", "other")
    and not col.endswith(LOWER_SUFFIX)
    and not col.endswith(UPPER_SUFFIX)
    and df[col].iloc[-1] >= 0.05
]

# --- Shared selections ---
nearest_date = alt.selection_point(
    nearest=True,
    on="pointerover",
    fields=["date"],
    empty=False,
)

# --- Build one chart per party ---
ymax = 1.1 * df.drop("date", axis=1).max().max()
y_scale = alt.Scale(domain=[0, ymax])

charts = []

for party in parties_in_data:
    color = PARTIES[party]["color"]

    # Columns for this party
    lower_col = f"{party}{LOWER_SUFFIX}"
    upper_col = f"{party}{UPPER_SUFFIX}"
    has_ci = lower_col in df.columns and upper_col in df.columns

    # Build per-party dataframe
    cols = ["date", party]
    if has_ci:
        cols += [lower_col, upper_col]
    party_df = df[cols].copy()
    party_df = party_df.rename(
        columns={
            party: "value",
            lower_col: "lower",
            upper_col: "upper",
        }
    )

    base = alt.Chart(party_df).encode(
        x=alt.X("date:T", title="Date", axis=alt.Axis(format="%d %b")),
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
        label_expr = (
            alt.expr.format(alt.datum.value, ".1f")
            + " ["
            + alt.expr.format(alt.datum.lower, ".1f")
            + ", "
            + alt.expr.format(alt.datum.upper, ".1f")
            + "]"
        )
    else:
        label_expr = alt.expr.format(alt.datum.value, ".1f")

    # Centre line
    line = base.mark_line(
        color=color,
        strokeWidth=2,
        interpolate="monotone",
    ).encode(
        y=alt.Y("value:Q", title="Support [%]"),
    )

    # Vertical rule on hover
    rule_points = (
        base.mark_circle(opacity=0)
        .encode(
            y=alt.Y("value:Q"),
        )
        .add_params(nearest_date)
    )

    rule = (
        base.mark_rule(color="gray", strokeWidth=1)
        .encode(
            x="date:T",
        )
        .transform_filter(nearest_date)
    )

    value_label = (
        base.mark_text(
            dx=-2,
            dy=-HEIGHT // 2,
            align="right",
            fontSize=12,
            color=color,
            fontWeight="bold",
            stroke="black",
            strokeWidth=0.25,
        )
        .encode(text=alt.Text("value:Q", format=".1f"))
        .transform_filter(nearest_date)
    )

    ci_label = (
        base.mark_text(
            dx=-2,
            dy=-HEIGHT // 2 + 12,
            align="right",
            fontSize=8,
            color="grey",
        )
        .encode(
            text=alt.Text("ci:N"),
        )
        .transform_filter(nearest_date)
        .transform_calculate(ci=alt.expr.format(alt.datum.lower, ".1f") + "–" + alt.expr.format(alt.datum.upper, ".1f"))
    )

    layers = [rule_points, rule, value_label, ci_label]
    if has_ci:
        layers.append(band)
    layers += [line]

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
charts = [charts[i] for i in np.argsort(-df[parties_in_data].iloc[-1]).values]  # reorder from highest support to lowest
final_chart = (
    alt.concat(*charts, columns=3)
    .configure_axis(
        labelFontSize=10,
        titleFontSize=12,
    )
    .configure_view(
        stroke=None,
    )
)

final_chart.save("js/polling_chart_multiples.json")
final_chart.save("polling_chart_multiples.png", scale_factor=2.0)
