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
filename = dataDir + "BEV_IEA2020.csv"
year,bev = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=2)

modelParameters = np.polyfit(year,np.log(bev),1)
modelFuncBEV = np.poly1d(modelParameters)

modelYear = range(2010,2031)
modelBEV = np.exp(modelFuncBEV(modelYear))

plt.yscale('log')
plt.plot(year,bev,linewidth=0, marker='o')
plt.plot(modelYear,modelBEV)
plt.plot([2010,2030],[1000,1000])
plt.xlabel('Year')
plt.ylabel('Lithium battery cost (USD/kWh)')
