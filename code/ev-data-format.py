#!/usr/bin/env python
# python3
"""
    reformat BEV data downloaded from IEA 
    https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
__author__ = "Rupert Sutherland"

dataDir = '../data/ev/'
filename = dataDir + 'IEA-EV-dataEV_salesHistoricalCars.csv'

df = pd.read_csv(filename, skiprows=1)

sel1 = df[(df['parameter']=='EV stock') & 
          (df['unit']=='Vehicles') ]

sel2 = sel1[sel1['region']=='China']
sel2.to_csv(dataDir+'china_ev.csv',index=False)
sel2 = sel1[(sel1['region']=='China') & (sel1['powertrain']=='BEV')]
sel2.to_csv(dataDir+'china_bev.csv',index=False)
sel2 = sel1[(sel1['region']=='China') & (sel1['powertrain']=='PHEV')]
sel2.to_csv(dataDir+'china_phev.csv',index=False)


sel3 = sel1[sel1['region']=='World']
sel3.to_csv(dataDir+'world_ev.csv',index=False)
sel3 = sel1[(sel1['region']=='World') & (sel1['powertrain']=='BEV')]
sel3.to_csv(dataDir+'world_bev.csv',index=False)
sel3 = sel1[(sel1['region']=='World') & (sel1['powertrain']=='PHEV')]
sel3.to_csv(dataDir+'world_phev.csv',index=False)

