
import pandas as pd

#reading the data
display = pd.read_csv('main.csv')

# print (display[['Team','Yellow Cards','Red Cards']])

data = display.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

print(data[['Team','Yellow Cards', 'Red Cards']])

#Code done by Anurag 