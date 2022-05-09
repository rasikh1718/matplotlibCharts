from turtle import color
from matplotlib import pyplot
companies=['hp','acer','lenovo','dell','apple']
itemsold=[122,54,88,121,158]
clrs=['red','green','blue','yellow','gray']

pyplot.bar(companies,itemsold,color=clrs)
pyplot.xlabel('laptop')
pyplot.ylabel('sales')
pyplot.title('laptop sales in 2022')
pyplot.show()