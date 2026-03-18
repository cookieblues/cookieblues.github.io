import numpy as np
import pandas as pd


def calculate_mandates(df: pd.DataFrame) -> pd.DataFrame:
    adjusted_percentage = df.div(df.sum(axis=1), axis=0)
    above_barrier = adjusted_percentage >= 0.02
    mandate_key = adjusted_percentage[above_barrier].sum(axis=1) / 175
    total_allowed_n_mandates = adjusted_percentage[above_barrier].div(mandate_key, axis=0)
    n_mandates = pd.DataFrame(np.floor(total_allowed_n_mandates))
    leftover_mandates = 175 - n_mandates.sum(axis=1)
    mandate_residue = (total_allowed_n_mandates - n_mandates).rank(axis=1, method="first", ascending=False)
    additional_mandates = mandate_residue.le(leftover_mandates, axis=0)
    n_mandates = n_mandates.fillna(0)
    n_mandates += additional_mandates
    return n_mandates.astype(int)
