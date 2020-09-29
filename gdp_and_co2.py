import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('wdi_small_tidy_2015.csv')
df2 = df[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]

plt.scatter('GDP per capita (constant 2010 US$)','Mortality rate, infant (per 1,000 live births)', data = df2)