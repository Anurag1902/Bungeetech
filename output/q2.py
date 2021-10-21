import pandas as pd

#reading the data
display = pd.read_csv('main.csv')

#using group by and calculating min and max
data = display.groupby('occupation')['age'].agg(['min','max'])


print (data)

#Code done by Anurag 