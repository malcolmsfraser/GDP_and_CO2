import pandas as pd 
import matplotlib.pyplot as plt 

# loading csv into df2
df = pd.read_csv('wdi_small_tidy_2015.csv')
# extracting desired columns from df1 into df2
df2 = df[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]

# plotting
plt.scatter('GDP per capita (constant 2010 US$)','Mortality rate, infant (per 1,000 live births)', data = df2)