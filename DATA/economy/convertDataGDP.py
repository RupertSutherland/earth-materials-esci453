#!python3

"""
    Converts a horrible format from 
    https://data.worldbank.org/indicator/NY.GDP.PCAP.KD
    into standard format with two columns: year; gdp per capita
    
    The gdp/capita data are inflation adjusted by World Bank to 2010 USD.

    The data can be downloaded as a csv file, but are difficult to load. 
    The first 3 lines are general metadata about the file. 
    The first 4 columns are: 'Country Name', 'Country Code', 'Indicator Name', 
    'Indicator Code'; and these names appear in row 4. 
    However row 4 also contains the 'year' value, and so the number of columns 
    increases by one each year that the file is updated - we will need to 
    figure out how many columns the file has. 
    Each row (5 onwards) is for a specific country/indicator combination 
    (as specified in first 4 columns), and corresponds to the year given in the 
    corresponding column in row 4.
    
    To figure out how many columns (`num_cols`) the csv file has, we use the 
    fact that every row, including the first, has the same number of column 
    delimiters ','. 
    We read the first line (creates a string), split it using the in-built 
    string function `split()`, and then use the `len()` function to find out 
    how many pieces it was split into (length of the list created by split).
    
    The main block of data (year and gdp per capita values) can all be loaded 
    as floating point values (the default type), but we need to specify to skip 
    the first 3 header lines, and to load the full range of columns from 4 
    (remember python is zero-based, so this is the fifth column) to `num_cols`.
    
    The 'Country Name' value is a good way to identify specific data we are 
    interested in, so we load that separately. Note that the data type needs to 
    be specified. `dtype = 'U20'` tells the function to decode the values in 
    the file as 'unicode text', which is basically a normal text string up to 
    20 characters long (see https://en.wikipedia.org/wiki/Unicode). 
    You could increase the value to 30 or more as you like, if some names are 
    longer, but it would require that more memory in the computer is allocated.    
    
"""
import numpy as np

filename = 'gdp-per-capita-world-bank-usd2010.csv'

with open(filename, 'r') as f:
    num_cols = len(f.readline().split(','))
    
gdpData = np.genfromtxt(filename, delimiter=',', skip_header=3,
                        usecols = range(4,num_cols) )

region = np.genfromtxt(filename, delimiter=',', skip_header=3,
                       usecols=(0,), dtype = 'U20')
gdpYear = gdpData[0]

iWorld = np.where(region == 'World')[0][0]

gdpWorld = gdpData[iWorld]

np.savetxt('gdp-per-capita-world-usd2010.csv',
           np.column_stack((gdpYear,gdpWorld)),
           fmt=['%i','%.2f'],
           delimiter=',',
           header='gdpYear,gdpPerCapita')

