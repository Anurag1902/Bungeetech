import pandas as pd
import numpy as np

# reading the data
display = pd.read_csv('main.csv')

#group by year with the range of 10 years and summing the coloumns except Population
data = display.groupby(np.floor(display['Year']/10) * 10)[['Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']].sum();

#adding population coloumn with the max value 
data['Population'] = display['Population'].groupby(np.floor(display['Year']/10) * 10).max()

print(data)
#Code done by Anurag