from matplotlib import pyplot as pl

x=[1,2,3,4,5]
y=[1,4,9,16,25]
z=[1,8,27,64,125]

fig,axes=pl.subplots(1,2)
axes[0].plot(x,y,'g--')
axes[0].scatter(x,y)

axes[1].plot(x,z,'r--')
axes[1].scatter(x,z)
pl.show()