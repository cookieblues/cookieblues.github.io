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
functions {
  vector fix_negative_probs(int n_parties, vector res) {
    vector[n_parties] temp;
    print(res);
    temp = 0.0005 + res - min(res);
    print(temp);
    temp = temp / sum(temp);
    print(temp);
    print(3);
    return(temp);
  }
}

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
    matrix<lower=-0.1,upper=0.1>[n_houses, n_parties] aHouseAdjustment;
    matrix<lower=-0.1,upper=0.1>[n_houses, n_parties] tHouseAdjustment;
    for(p in 1:n_parties) // included parties sum to zero 
      aHouseAdjustment[,p] = houseAdjustment[,p] - mean(houseAdjustment[,p]);
    for(h in 1:n_houses) // included houses sum to zero 
      tHouseAdjustment[h,] = aHouseAdjustment[h,] - mean(aHouseAdjustment[h,]);
}

model{
    // -- house effects model
    for(h in 1:n_houses) {
        houseAdjustment[h] ~ normal(0, 0.01);
    }

    // -- temporal model
    hidden_voting_intention[1] ~ dirichlet(startingPoint * startingPointCertainty);
    // hidden_voting_intention[discontinuity] ~ dirichlet(startingPoint * startingPointCertainty);
    
    for (day in 2:n_days)
      hidden_voting_intention[day] ~ dirichlet(hidden_voting_intention[day-1] * transmissionStrength);

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
    for(poll in 1:n_polls) {
      print(1);
      print(tHouseAdjustment[house[poll],]');
      print(hidden_voting_intention[poll_day[poll]]);
      print(2);
      y[poll] ~ multinomial(fix_negative_probs(n_parties, hidden_voting_intention[poll_day[poll]] + tHouseAdjustment[house[poll],]'));
    }
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


GAUSSIAN_PROCESS = """
data {
    // data size
    int<lower=1> n_polls;
    int<lower=1> n_days;
    int<lower=1> n_houses;
    int<lower=1> n_parties;
    real<lower=0> pseudoSampleSigma;

    // Centreing factors 
    real<lower=0> center;
    real centreing_factors[n_parties];

    // poll data
    real<lower=0> centered_obs_y[n_parties, n_polls]; // poll data
    int<lower=1,upper=n_houses> house[n_polls]; // polling house
    int<lower=1,upper=n_days> poll_day[n_polls]; // day on which polling occurred
    // vector<lower=0> [n_polls] poll_qual_adj; // poll quality adjustment

    //exclude final n parties from the sum-to-zero constraint for houseEffects
    //int<lower=0> n_exclude;

    // period of discontinuity and subsequent increased volatility event
    // int<lower=1,upper=n_days> discontinuity; // start with a discontinuity
    // int<lower=1,upper=n_days> stability; // end - stability restored

    // day-to-day change
    real<lower=0> sigma;
    // real<lower=0> sigma_volatile;

    // TPP preference flows
    // vector<lower=0,upper=1>[n_parties] preference_flows_2010;
    // vector<lower=0,upper=1>[n_parties] preference_flows_2013;
    // vector<lower=0,upper=1>[n_parties] preference_flows_2016;
}

transformed data {
    int<lower=1> n_include = n_houses;
}

parameters {
    matrix<lower=50,upper=150>[n_days, n_parties] centre_track;
    matrix<lower=-10,upper=10>[n_houses, n_parties] pHouseEffects;
}

transformed parameters {
    matrix<lower=-10,upper=10>[n_houses, n_parties] houseEffects;
    for(p in 1:n_parties) {
        houseEffects[1:n_houses, p] = pHouseEffects[1:n_houses, p] - mean(pHouseEffects[1:n_include, p]);
    }
}

model{
    for (p in 1:n_parties) {
        // -- house effects model
        pHouseEffects[, p] ~ normal(0, 5.0); // weakly informative PRIOR

        // -- temporal model - with a discontinuity followed by increased volatility
        centre_track[1, p] ~ normal(center, 1); // weakly informative PRIOR
        centre_track[2:n_days, p] ~ normal(centre_track[1:(n_days-1), p], sigma);

        // centre_track[2:(discontinuity-1), p] ~ 
        //     normal(centre_track[1:(discontinuity-2), p], sigma);
        // centre_track[discontinuity, p] ~ normal(center, 15); // weakly informative PRIOR
        // centre_track[(discontinuity+1):stability, p] ~ 
        //     normal(centre_track[discontinuity:(stability-1), p], sigma_volatile);
        // centre_track[(stability+1):n_days, p] ~ 
        //     normal(centre_track[stability:(n_days-1), p], sigma);

        // -- observational model
        // print(p);
        // print(houseEffects[house, p]);
        // print(centre_track[poll_day, p]);
        centered_obs_y[p,] ~ normal(houseEffects[house, p] + centre_track[poll_day, p], pseudoSampleSigma);
    }
}

generated quantities {
    matrix[n_days, n_parties]  hidden_vote_share;
    // vector [n_days] tpp2010;
    // vector [n_days] tpp2013;
    // vector [n_days] tpp2016;

    for (p in 1:n_parties) {
        hidden_vote_share[,p] = centre_track[,p] - centreing_factors[p];
    }

    // aggregated TPP estimates based on past preference flows
    // for (d in 1:n_days){
    //     // note matrix transpose in next three lines
    //     tpp2010[d] = sum(hidden_vote_share'[,d] .* preference_flows_2010);
    //     tpp2013[d] = sum(hidden_vote_share'[,d] .* preference_flows_2013);
    //     tpp2016[d] = sum(hidden_vote_share'[,d] .* preference_flows_2016);
    // }
} 
"""