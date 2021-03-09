import pandas as pd

from config import *
from src import jackman2005


df = pd.DataFrame()

for party_name in PARTIES.keys():
    posterior_df = jackman2005(party_name)
    df = pd.concat([df, posterior_df])

breakpoint()



# import pandas as pd
# import pystan


# df = pd.read_csv("polls.csv")

# # Create date column
# df["date"] = pd.to_datetime(df[["year", "month", "day"]])
# df = df.sort_values(by="date", ascending=True)
# df.index = df["date"]

# # Go from last election
# df = df.loc[df.index > "2019-06-05"].copy()

# df = df.drop(["year", "month", "day", "date"], axis=1)
# df["time"] = (df.index-df.index[0]).days


# # Factorize pollsters
# pollsters, uniq_pollsters = pd.factorize(df["pollingfirm"])
# df["pollingfirm"] = pollsters

# # Impute missing sample sizes
# df["n"] = df["n"].fillna(1000)


# df["party_a_se"] = df["party_a"] * (100-df["party_a"]) / df["n"]

# # Model: https://jrnold.github.io/bugs-examples-in-stan/campaign.html
# stan_model = """
# data {
#   int N;                // number of polls
#   int T;                // number of days
#   vector[N] y;
#   vector[N] s;
#   int time[N];          // days on which polls are made
#   int H;                // number of pollsters
#   int house[N];         // pollster identifier
#   // initial and final values
#   real alpha_init;
#   real alpha_final;
#   real delta_loc;
#   real zeta_scale;
#   real tau_scale;
# }
# parameters {
#   vector[T - 1] omega;
#   real tau;
#   vector[H] delta_raw;
#   real zeta;
# }
# transformed parameters {
#   vector[H] delta;
#   vector[T - 1] alpha;
#   vector[N] mu;
#   // this is necessary. If not centered the model is unidentified
#   delta = (delta_raw - mean(delta_raw)) / sd(delta_raw) * zeta;
#   alpha[1] = alpha_init;
#   for (i in 2:(T-1)) {
#     alpha[i] = alpha[i - 1] + tau * omega[i - 1];
#   }
#   for (i in 1:N) {
#     mu[i] = alpha[time[i]] + delta[house[i]];
#   }
# }
# model {
#   // house effects
#   delta_raw ~ normal(0., 1.);
#   zeta ~ normal(0., zeta_scale);
#   // latent state innovations
#   omega ~ normal(0., 1.);
#   // scale of innovations
#   tau ~ cauchy(0, tau_scale);
#   // final known effect
#   //alpha_final ~ normal(alpha[T - 1], tau);
#   // daily polls
#   y ~ normal(mu, s);
# }
# """

# # Prepare data for stan
# stan_data = {
#     "N": df.shape[0],
#     "T": df["time"].max()+2,
#     "y": df["party_a"],
#     "s": df["party_a_se"],
#     "time": df["time"]+1,
#     "H": len(uniq_pollsters),
#     "house": pollsters+1,
#     "alpha_init": 25.9,
#     "alpha_final": 30.0,
#     "delta_loc": 0,
#     "zeta_scale": 5,
#     "tau_scale": 3,
# }

# # Run stan
# posterior = pystan.StanModel(model_code=stan_model)
# fit = posterior.sampling(data=stan_data, chains=4, iter=1000, seed=1)
# alpha = fit["alpha"]
# posterior_df = fit["alpha"]
# posterior_df.to_csv("asd.csv", index=False)