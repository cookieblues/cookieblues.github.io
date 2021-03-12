from pathlib import Path


DATA_DIRECTORY = Path("data")
MODEL_DIRECTORY = Path("models")

PREV_ELECTION_DATES = [
    "2019-06-05"
]

PREV_ELECTION_RESULTS = {
    "Socialdemokratiet": 25.9,
    "Radikale_Venstre": 8.6,
    "Det_Konservative_Folkeparti": 6.6,
    "Nye_Borgerlige": 2.4,
    "Klaus_Riskær_Pedersen": 0.8,
    "Socialistisk_Folkeparti": 7.7,
    "Veganerpartiet": 0.0,
    "Liberal_Alliance": 2.3,
    "Kristendemokraterne": 1.7,
    "Dansk_Folkeparti": 8.7,
    "Stram_Kurs": 1.8,
    "Venstre": 23.4,
    "Enhedslisten": 6.9,
    "Alternativet": 3.0
}

PARTIES = {
    "Socialdemokratiet": "party_a",
    "Radikale_Venstre": "party_b",
    "Det_Konservative_Folkeparti": "party_c",
    "Nye_Borgerlige": "party_d",
    "Klaus_Riskær_Pedersen": "party_e",
    "Socialistisk_Folkeparti": "party_f",
    "Veganerpartiet": "party_g",
    "Liberal_Alliance": "party_i",
    "Kristendemokraterne": "party_k",
    "Dansk_Folkeparti": "party_o",
    "Stram_Kurs": "party_p",
    "Venstre": "party_v",
    "Enhedslisten": "party_oe",
    "Alternativet": "party_aa"
}

# Model: https://jrnold.github.io/bugs-examples-in-stan/campaign.html
JACKMAN_2005 = """
data {
  int N;                // number of polls
  int T;                // number of days
  vector[N] y;
  vector<lower=0>[N] s;
  int time[N];          // days on which polls are made
  int H;                // number of pollsters
  int house[N];         // pollster identifier
  // initial and final values
  real alpha_init;
  //real alpha_final;
  real delta_loc;
  real zeta_scale;
  real tau_scale;
}
parameters {
  vector<lower=0>[T - 1] omega;
  real tau;
  vector[H] delta_raw;
  real zeta;
}
transformed parameters {
  vector[H] delta;
  vector[T - 1] alpha;
  vector[N] mu;
  // this is necessary. If not centered the model is unidentified
  delta = (delta_raw - mean(delta_raw)) / sd(delta_raw) * zeta;
  alpha[1] = alpha_init;
  for (i in 2:(T-1)) {
    alpha[i] = alpha[i - 1] + tau * omega[i - 1];
  }
  for (i in 1:N) {
    mu[i] = alpha[time[i]] + delta[house[i]];
  }
}
model {
  // house effects
  delta_raw ~ normal(0., 1.);
  zeta ~ normal(0., zeta_scale);
  // latent state innovations
  omega ~ normal(0., 1.);
  // scale of innovations
  tau ~ cauchy(0, tau_scale);
  // final known effect
  //alpha_final ~ normal(alpha[T - 1], tau);
  // daily polls
  y ~ normal(mu, s);
}
"""


# Dirichlet-multinomial process
DIRICHLET_MULTINOMIAL_PROCESS = """
data {
    // data size
    int<lower=1> n_polls;
    int<lower=1> n_days;
    int<lower=1> n_houses;
    int<lower=1> n_parties;
    // int<lower=1,upper=n_days> discontinuity;
    // int<lower=1,upper=n_days> stability;
    
    // key variables
    int<lower=1> psuedoSampleSize; // maximum sample size for y
    real<lower=1> transmissionStrength;
    real<lower=1> transmissionStrengthPostDiscontinuity;
    
    // give a rough idea of a staring point ...
    simplex[n_parties] startingPoint; // rough guess at series starting point
    int<lower=1> startingPointCertainty; // strength of guess - small number is vague
    
    // poll data
    int<lower=0,upper=psuedoSampleSize> y[n_polls, n_parties]; // a multinomial
    int<lower=1,upper=n_houses> house[n_polls]; // polling house
    int<lower=1,upper=n_days> poll_day[n_polls]; // day polling occured
    
    // TPP preference flows
    // vector<lower=0,upper=1>[n_parties] preference_flows_2010;
    // vector<lower=0,upper=1>[n_parties] preference_flows_2013;
    // vector<lower=0,upper=1>[n_parties] preference_flows_2016;
}

parameters {
    simplex[n_parties] hidden_voting_intention[n_days];
    matrix[n_houses, n_parties] houseAdjustment;
}

transformed parameters {
    matrix[n_houses, n_parties] aHouseAdjustment;
    matrix[n_houses, n_parties] tHouseAdjustment;
     for(p in 1:n_parties) // included parties sum to zero 
        aHouseAdjustment[,p] = houseAdjustment[,p] - mean(houseAdjustment[,p]);
     for(h in 1:n_houses) // included parties sum to zero 
        tHouseAdjustment[h,] = aHouseAdjustment[h,] - mean(aHouseAdjustment[h,]);
}

model{
    // -- house effects model
    for(h in 1:n_houses)
        houseAdjustment[h] ~ normal(0, 0.05); 
    
    // -- temporal model
    hidden_voting_intention[1] ~ dirichlet(startingPoint * startingPointCertainty);
    // hidden_voting_intention[discontinuity] ~ dirichlet(startingPoint * startingPointCertainty);
    
    for (day in 2:n_days)
        hidden_voting_intention[day] ~ 
              dirichlet(hidden_voting_intention[day-1] * transmissionStrength);

    // for (day in 2:(discontinuity-1))
    //     hidden_voting_intention[day] ~ 
    //         dirichlet(hidden_voting_intention[day-1] * transmissionStrength);
    // for (day in (discontinuity+1):stability)
    //     hidden_voting_intention[day] ~ dirichlet(hidden_voting_intention[day-1] * 
    //         transmissionStrengthPostDiscontinuity);
    // for (day in (stability+1):n_days)
    //     hidden_voting_intention[day] ~ dirichlet(hidden_voting_intention[day-1] * 
    //         transmissionStrength);
    
    // -- observed data model
    for(poll in 1:n_polls)
        y[poll] ~ multinomial(hidden_voting_intention[poll_day[poll]] + tHouseAdjustment[,house[poll]]);
}

generated quantities {
    // aggregated TPP estimates based on past preference flows
    // vector [n_days] tpp2010;
    // vector [n_days] tpp2013;
    // vector [n_days] tpp2016;

    // for (d in 1:n_days){
    //     tpp2010[d] = sum(hidden_voting_intention[d] .* preference_flows_2010);
    //     tpp2013[d] = sum(hidden_voting_intention[d] .* preference_flows_2013);
    //     tpp2016[d] = sum(hidden_voting_intention[d] .* preference_flows_2016);
    // }
}
"""
