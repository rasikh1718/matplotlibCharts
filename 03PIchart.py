
from matplotlib import pyplot

countries=['germany','russia','india','indonesia','england']
profit=[7020,2502,6524,3654,8594]

pyplot.pie(profit, labels=countries, autopct='%.2f%%')
pyplot.title('profit in 2021')
pyplot.show()
