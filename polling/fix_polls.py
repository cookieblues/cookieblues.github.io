import pandas as pd

party_names = [
    'Socialdemokratiet',
    'Radikale_Venstre',
    'Det_Konservative_Folkeparti',
    'Nye_Borgerlige',
    'Klaus_Riskær_Pedersen',
    'Socialistisk_Folkeparti',
    'Veganerpartiet',
    'Liberal_Alliance',
    'Kristendemokraterne',
    'Dansk_Folkeparti',
    'Stram_Kurs',
    'Venstre',
    'Enhedslisten',
    'Alternativet'
]

df = pd.read_csv('polls.csv', usecols=[
    'year',
    'month',
    'day',
    'party_a',
    'party_b',
    'party_c',
    'party_d',
    'party_e',
    'party_f',
    'party_g',
    'party_i',
    'party_k',
    'party_o',
    'party_p',
    'party_v',
    'party_oe',
    'party_aa'
])

today = pd.to_datetime("today").date()
start_date = today-pd.DateOffset(months=6)
six_months_range = pd.date_range(start_date, today, freq="1D")

df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df = df.sort_values(by='date', ascending=True)
df.index = df['date']
df = df.drop(['year', 'month', 'day', 'date'], axis=1)

### Get mean data
mean_df = df.copy()

# Fix duplicates
mean_of_dupes = mean_df[mean_df.index.duplicated(keep=False)].groupby(by='date').mean()
mean_df[mean_df.index.duplicated(keep=False)] = mean_of_dupes
mean_df = mean_df.drop_duplicates()

# Calc mean
mean_df = mean_df.rolling('14D', min_periods=0).mean().round(1)
mean_df.columns = party_names
mean_df = mean_df.reindex(pd.date_range(mean_df.index[0], today).date)
mean_df = mean_df.ffill()
mean_df = mean_df.loc[
    start_date <= mean_df.index,
    party_names
].copy()
mean_df.to_csv('mean_polls.csv')

### Get poll data
new_df = df.copy()
new_df.columns = party_names
new_df = new_df.loc[
    start_date <= new_df.index,
    party_names
].copy()

new_df.to_csv('fixed_polls.csv')

