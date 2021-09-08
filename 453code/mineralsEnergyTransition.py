#!/usr/bin/env python
# python3
"""
    ESCI 453 Notebook 12 exercises - minerals for energy transition
"""
import numpy as np

__author__ = "Rupert Sutherland"

npyDir = '../453notebooks/'

year = np.load(npyDir+'eYear.npy')
sel = np.logical_and(year >= 2020, year <= 2050)
np.save('year_ET.npy',year[sel])

newStorageNeededTWh = np.load(npyDir+'newStorageNeededTWh.npy')
# values in metric tons per TWh
Li = 1.5e5 * newStorageNeededTWh[sel]
Co = 1.5 * Li
Ni = 4.0 * Li
Mn = 2.5 * Li
Cu = 5.5 * Li
np.save('Li_storage.npy',Li)
np.save('Co_storage.npy',Co)
np.save('Ni_storage.npy',Ni)
np.save('Mn_storage.npy',Mn)
np.save('Cu_storage.npy',Cu)

newSolarInstallationGW = np.load(npyDir+'newSolarInstallationGW.npy')
# values in metric tons per GW
Cu = 3000 * newSolarInstallationGW[sel]
Ag =   60 * newSolarInstallationGW[sel]
np.save('Cu_solar.npy',Cu)
np.save('Ag_solar.npy',Ag)

newWindInstallationGW = np.load(npyDir+'newWindInstallationGW.npy')
# values in metric tons per GW
Cu = 6000 * newWindInstallationGW[sel]
Ni = 500 * newWindInstallationGW[sel]
Mn = 1000 * newWindInstallationGW[sel]
Cr = 700 * newWindInstallationGW[sel]
Mo = 100 * newWindInstallationGW[sel]
Zn = 6000 * newWindInstallationGW[sel]
np.save('Cu_wind.npy',Cu)
np.save('Ni_wind.npy',Ni)
np.save('Mn_wind.npy',Mn)
np.save('Cr_wind.npy',Cr)
np.save('Mo_wind.npy',Mo)
np.save('Zn_wind.npy',Zn)
