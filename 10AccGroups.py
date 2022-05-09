import pymysql
import pandas
from matplotlib import pyplot as pl

con=pymysql.connect(host='localhost',user='root',password='volkswagen',database='banktransdb')
qr="select acctype,sum(balance) 'total' from accounts group by acctype"

df=pandas.read_sql(qr,con)
#  from querie connection
print(df)

pl.bar(df['acctype'],df['total'])
pl.show()