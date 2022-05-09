from matplotlib import pyplot as p

companies=['hp','acer','asus','microsoft','dell','lenovo','apple']
itemssold=[362,59,247,128,489,621,158]
returns=[11,7,78,2,9,43,3]

p.plot(companies,itemssold,color='blue')
p.scatter(companies,itemssold,color='black')


p.plot(companies,returns,color='red')
p.scatter(companies,returns,color='purple')

p.show()