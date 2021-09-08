#!/usr/bin/env python
# python3
"""
    docstring
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
rc("font",size=10)

__author__ = "Rupert Sutherland"

'''
The file is difficult because one region 
"Bonaire, Sint Eustatius and Saba"
contains a comma, but it is csv format

pandas can cope with this better than numpy loadtxt or genfromtxt
'''

irena = pd.read_csv("../DATA/energy-renewable/IRENA_data_202108.csv")

sel = np.logical_and(irena["Electricity Generation (GWh)"] > 0,
                     irena["Electricity Installed Capacity (MW)"] > 0)

#sel = np.logical_and(sel,irena["Technology"].str.contains('photovoltaic'))
sel = np.logical_and(sel,irena["Technology"].str.contains('wind'))


capacity = irena["Electricity Installed Capacity (MW)"][sel]
generation = irena["Electricity Generation (GWh)"][sel]

params = np.polyfit(capacity,generation,1)
modelGeneration = np.poly1d(params)(capacity)
gradient = params[0]

plt.scatter(capacity,generation)
plt.plot(capacity,modelGeneration)

print("Gradient generation/capacity (GWh/MW)",gradient,"params=",params)
'''
'''


