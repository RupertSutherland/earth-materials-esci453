#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot and model lithium battery costs
Created on Thu Jul 29 13:48:27 2021
@author: rupert
"""
import numpy as np
import matplotlib.pyplot as plt

# load the data file
dataDir = "../DATA/energy-renewable/"
filename = dataDir + "lithium-battery-costs-2020.csv"
year,cost = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=2)

modelParameters = np.polyfit(year,np.log(cost),1)
modelFuncCost = np.poly1d(modelParameters)

modelYear = range(2010,2031)
modelCost = np.exp(modelFuncCost(modelYear))

#plt.yscale('log')
plt.plot(year,cost,linewidth=0, marker='o')
plt.plot(modelYear,modelCost)
plt.xlabel('Year')
plt.ylabel('Lithium battery cost (USD/kWh)')
