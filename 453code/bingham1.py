#!/usr/bin/env python
# python3
"""
    load, analyze, plot data from Bingham Mine
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
rc("font",size=10)

__author__ = "Rupert Sutherland"
__credits__ = ["Rupert Sutherland",]
__license__ = "GPL"
__version__ = "1.1"
__maintainer__ = "Rupert Sutherland"
__email__ = "rupert.sutherland@vuw.ac.nz"
__status__ = "Prototype"
#-----------------------------------------------------------------------------

data = np.genfromtxt('../DATA/copper/BinghamCanyonMine.csv',
                  delimiter=',',skip_header=8)

# convert short tons to metric tons
convert = 0.907185

year = data[:,0]
ore = data[:,1] * convert
waste = data[:,2] * convert
Cu = data[:,4] * convert
Mo = data[:,5] * convert
gold = data[:,6] 
silver = data[:,7] 

strippingRatio = waste/ore
oreGrade = Cu/ore

priceGoldPerOz = 1800
goldTotalOz = np.sum(gold)*1000
goldTotalValue = goldTotalOz * priceGoldPerOz
print(goldTotalValue/1e9,'B$')

priceCu = 6000.0
CuTotalValue = priceCu * np.sum(Cu)
print(CuTotalValue/1e9,'B$')


plt.figure(figsize=(12,4))
plt.minorticks_on()
plt.xlabel('Time (years)')
#plt.ylabel('Bingham mine stripping ratio')
#plt.plot(year,strippingRatio)
plt.ylabel('Bingham mine ore grade')
plt.plot(year,oreGrade)

