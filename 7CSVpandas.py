from turtle import color
import pandas
from matplotlib import pyplot as pl
df=pandas.read_csv("covid-usa.csv")
# df=pandas.read_csv("covid-usa.csv")
# print(df)
pl.plot(df['month'],df['cases'])
pl.scatter(df['month'],df['deaths'])

pl.plot(df['month'],df['deaths'])
pl.scatter(df['month'],df['deaths'],color='red')

pl.title('show pandas and CSV')
pl.show()