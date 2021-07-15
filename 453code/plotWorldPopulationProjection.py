import numpy as np
import matplotlib.pyplot as plt

dataDir = '../DATA/world-population/'
filename = dataDir + 'world_population_v2020.csv'
    
filename = dataDir + 'UN2019-population-projection-world-Low.csv'
year,pop = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=1)
plt.plot(year,pop/1000,linestyle='--',color='black')

filename = dataDir + 'UN2019-population-projection-world-High.csv'
year,pop = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=1)
plt.plot(year,pop/1000,linestyle='--',color='black')

filename = dataDir + 'UN2019-population-projection-world-Medium.csv'
year,pop = np.loadtxt(filename, delimiter=',',unpack=True,
                      usecols=[0,1],skiprows=1)
plt.plot(year,pop/1000,linestyle='-',linewidth=3,color='black')

plt.xlabel('Year')
plt.ylabel('Population (millions)')

