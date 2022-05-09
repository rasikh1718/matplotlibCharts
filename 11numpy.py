import numpy
from matplotlib import pyplot as pl

arr=numpy.random.randint(1,50,35)
arrsq=arr**2

print(arr)
print(arrsq)

pl.scatter(arr,arrsq)
pl.show()