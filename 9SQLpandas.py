import pymysql
import pandas
from matplotlib import pyplot as pl

con=pymysql.connect(host='localhost',user='root',password='volkswagen',database='banktransdb')
qr=("select * from products")

df=pandas.read_sql(qr,con)
#print(df)

pl.bar(df['prodid'],df['price'])
pl.show()

