import pandas as pd
import numpy as np

# reading the data
display = pd.read_csv('main.csv')

#converting the given 
display.Year = pd.to_datetime(display.Year, format = '%Y')
display.head()
#
display.set_index('Year', drop=True, inplace=True)
display.head()

data = display.resample('10AS').sum()
data['Population'] = display['Population'].resample('10AS').max()
print (data)

#Code done by Anurag