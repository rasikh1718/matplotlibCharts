from matplotlib import pyplot as pl
import pandas
import ssl

url='https://restapi.sohamglobal.in/api/accounts'
ssl._create_default_https_context=ssl._create_unverified_context
df=pandas.read_json(url)
#print(df)
df1=df[df['AccountType']=='saving']
pl.scatter(df1['AccountNumber'],df1['Balance'])
pl.show()