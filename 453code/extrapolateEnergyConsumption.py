import numpy as np
import matplotlib.pyplot as plt

codeDir = '../453notebooks/'
t = np.load(codeDir+'t.npy')
E = np.load(codeDir+'E.npy')
N = np.load(codeDir+'N.npy')
energyPerDollar = np.load(codeDir+'energyPerDollar.npy')
gdpPerCapita = np.load(codeDir+'gdpPerCapita.npy')

# Model and extrapolate raw energy consumption
polynomialOrder = 2
startYear = 1950
select = np.logical_and(t >= startYear, t <= 2018)
modelParameters = np.polyfit(t[select],E[select],polynomialOrder)
modelFuncEnergy = np.poly1d(modelParameters)
energyExtrapolated = modelFuncEnergy(t)

# Model = E/$ * $/person * N

# $/person
polynomialOrder = 1
select = np.logical_not(np.isnan(gdpPerCapita))
modelParameters = np.polyfit(t[select],gdpPerCapita[select],polynomialOrder)
modelFuncGdpPC = np.poly1d(modelParameters)
modelDollarsPerPerson = modelFuncGdpPC(t)

# E/$
polynomialOrder = 1
select = np.logical_not(np.isnan(energyPerDollar))
modelParameters = np.polyfit(t[select],np.log(energyPerDollar[select]),polynomialOrder)
modelFuncLogEnergyPerDollar = np.poly1d(modelParameters)
modelEnergyPerDollar = np.exp(modelFuncLogEnergyPerDollar(t))

modelEnergy = modelEnergyPerDollar * modelDollarsPerPerson * N/1000

# Plot
plt.figure(figsize=[14,7])
plt.plot(t, E, marker='o',
         label='Energy consumption data')
plt.plot(t, energyExtrapolated,
         label='Energy data extrapolated (quadratic)')
plt.plot(t, modelEnergy,
         label='Energy consumption = E/dollar * dollar/person * N')
plt.xlabel('Year')
plt.ylabel('Energy consumption (MWh/yr)')
plt.legend()

np.save('energy2100quadratic.npy', energyExtrapolated)
np.save('energy2100model1.npy', modelEnergy)
           
