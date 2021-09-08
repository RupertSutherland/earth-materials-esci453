#!/usr/bin/env python
# python3
"""
    ESCI 453 Notebook 12: minerals for energy transition
    Load and plot mineral needs - starter for class
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
rc("font",size=10,family='Arial')

__author__ = "Rupert Sutherland"

year = np.load('year_ET.npy')

# All units are metric tons
Ag = np.load('Ag_solar.npy')
Co = np.load('Co_storage.npy')
Cr = np.load('Cr_wind.npy')
Cu = np.load('Cu_wind.npy')+np.load('Cu_solar.npy')+np.load('Cu_storage.npy')
Li = np.load('Li_storage.npy')
Mn = np.load('Mn_storage.npy')+np.load('Mn_wind.npy')
Mo = np.load('Mo_wind.npy')
Ni = np.load('Ni_storage.npy')+np.load('Ni_wind.npy')
Zn = np.load('Zn_wind.npy')

demand = [Ag, Co, Cr, Cu, Li, Mn, Mo, Ni, Zn]
name = ['Ag','Co','Cr','Cu','Li','Mn','Mo','Ni','Zn']
symbol = ['$Ag$','$Co$','$Cr$','$Cu$','$Li$','$Mn$','$Mo$','$Ni$','$Zn$']
#symbol = ['*','o','^','+','x','v','s','$N$','$Z$']
'''
# USGS World mine production and reserves (metric tons)
# https://www.usgs.gov/centers/nmic/commodity-statistics-and-information
USD/ton
Note units change for different elements
Li carbonate corrected for mass wt% 2*6.94/73.89 = 0.188
Mn corrected for 44% Mn ore value
'''
# Conversions to metric tons
troyOz = 29166.7
lb = 2204.62
kg = 1000.
production2019 = [27000, 144000, 44800000, 20400000, 86000, 19600000, 
                  294000, 2610000, 12700000]
reserves2019 = [560000, 7000000, 570000000, 870000000, 21000000, 1300000000, 
                18000000, 94000000, 250000000]
price2021 = [17.17*troyOz, 15*lb, 10393, 2.72*lb, 12700*0.188, 5.63*0.44, 
             26.5*kg, 13903, 1.2*lb]

for i in range(9):
    plt.plot(demand[i].max()/reserves2019[i],
             demand[i].max()/production2019[i],
             marker=symbol[i], markersize=10, linestyle='',
             label=name[i])

plt.xlabel('Peak demand / reserves in 2019')
plt.ylabel('Peak production multiplier (2036/2019)')
plt.legend()
plt.minorticks_on()

plt.savefig('mineralsET.pdf')
