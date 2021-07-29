#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot and model lithium battery costs
Created on Thu Jul 29 13:48:27 2021
@author: rupert
"""
import numpy as np
import matplotlib.pyplot as plt

def logisticGrowthAnalytic(k,P,N0,t):
    '''
    Given the growth rate (k), carrying capacity (P), and initial population
    value (N0), generate an array of population (N) at various times (t), 
    based on analytical solution of the logistic growth equation. 
    Assumes k and P are not functions of t or N.

    Parameters
    ----------
    k : float
        Growth rate parameter.
    P : float
        Carrying capacity.
    N0 : float
        Initial population value (t=0).
    t : ndarray
        Time array.

    Returns
    -------
    N : ndarray
        Population value at time t

    '''
    return P / (1 + ((P-N0)/N0)*np.exp(-k*t))

# load the data file
dataDir = "../DATA/energy-renewable/"
filename = dataDir + "BEV_IEA2020.csv"
year,bev = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=2)

modelParameters = np.polyfit(year,np.log(bev),1)
modelFuncBEV = np.poly1d(modelParameters)

modelYear = np.arange(2010,2041)
modelExponentialBEV = np.exp(modelFuncBEV(modelYear))

k = modelParameters[0]
P = 1000.
N0 = modelExponentialBEV[0]
t = modelYear - 2010
modelLogisticBEV = logisticGrowthAnalytic(k,P,N0,t)

#plt.yscale('log')
plt.ylim([0,2000])
plt.plot(year,bev,linewidth=0, marker='o')
plt.plot(modelYear,modelExponentialBEV)
plt.plot(modelYear,modelLogisticBEV)
plt.plot([2010,2040],[1000,1000])
plt.xlabel('Year')
plt.ylabel('Lithium battery cost (USD/kWh)')
