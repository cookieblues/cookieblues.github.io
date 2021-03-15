import pandas as pd

from config import *
from src import gaussian_process


posterior_df = gaussian_process()
posterior_df.to_csv("data/interim/gaussian_posterior.csv", index=False)
