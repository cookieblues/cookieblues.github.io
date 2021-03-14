import pandas as pd

from config import *
from src import dirichlet_multinomial_process


posterior_df = dirichlet_multinomial_process()
#posterior_df.to_csv(DATA_DIRECTORY / "processed/mean_polls.csv", index_label="date")

