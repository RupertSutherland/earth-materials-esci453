#!/usr/bin/env python
# python3
__author__ = "Rupert Sutherland"
"""
    Extracts global BEV stock from IEA data file downloaded from
    https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer
"""
import pandas as pd

fName = 'IEA-EV-dataEV salesHistoricalCars.csv'

# Read file into a pandas dataframe
df = pd.read_csv(fName)

dfSel = df.loc[(df['region'] == 'World') & (df['parameter'] == 'EV stock') 
               & (df['powertrain'] == 'BEV')]

dfSel.to_csv('BEV_IEA2023.csv')
