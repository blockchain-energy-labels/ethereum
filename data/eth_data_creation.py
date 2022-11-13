# Ethereum data creation script
# emissions and energy csv files are before the merge to proof of stake ETH

import pandas as pd
import numpy as np
#take original hash rate and format so easy to turn into json
def hash_rates_to_csv(df):
    dates = df['Date'].to_numpy()
    hashrates =  df['Value'].to_numpy()
    
    csvarr = []
    for i in range(len(dates)): # len(dates) == len(hashrates)
        csvarr.append((dates[i], hashrates[i]))
    pd.DataFrame(csvarr).to_csv("eth_hash_rates.csv", index = False)

def emissions_to_csv(df):
    dates = df["Date"].to_numpy()
    low, high, best = df["lower"].to_numpy(), df["upper"].to_numpy(), df["best"].to_numpy()
    values = []
    for i in range(len(low)): # len(low) == len(high) == len(best)
        avg =  ( low[i] + high[i] + best[i] ) / 3
        values.append(avg)

    csvarr = []
    for i in range(len(values)):
        csvarr.append((dates[i], values[i]))
    pd.DataFrame(csvarr).to_csv("eth-emissions.csv")

if __name__ == "__main__":
    hash_rates_df = pd.read_csv("data/Ethereum-all-time-hash-rate.csv")
    market_prices_df = pd.read_csv("data/Ethereum-all-time-market-price.csv")
    state_emission_factors_df = pd.read_csv("data/state_emission_factor.csv")
    emissions_df = pd.read_csv("data/Ethereum-emissions.csv")

    #hash_rates_to_csv(hash_rates_df)
    emissions_to_csv(emissions_df)
    

    
