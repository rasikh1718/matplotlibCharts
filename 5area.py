# from cProfile import label
# from calendar import month
# from matplotlib import pyplot as py
# months=['jan','feb','mar','apr']
# inf=[14020,11410,20540,13241]
# adm=[7310,6325,1125,8652]
# death=[2550,5000,4200,3080]
# py.plot([],[],color='green',label='infection',linewidth=5)
# py.plot([],[],color='blue',label='admited',linewidth=5)
# py.plot([],[],color='red',label='death',linewidth=5)

# py.stackplot(month,death,adm,inf,colors=['red','blue','green'])
# py.xlabel('month')
# py.ylabel('patient')
# py.legend()
# py.title('corona summary 2021')
# py.show()

from matplotlib import pyplot as pl

months=['jan','feb','mar','apr']
inf=[14020,11410,19780,24570]
adm=[7310,6190,5820,15250]
deaths=[3618,1529,2630,7180]

pl.plot([],[],color='green',label='infections',linewidth=5)
pl.plot([],[],color='blue',label='admitted',linewidth=5)
pl.plot([],[],color='red',label='deaths',linewidth=5)

pl.stackplot(months,deaths,adm,inf,colors=['red','blue','green'])

pl.xlabel('Months')
pl.ylabel('patients')
pl.title('corona in 2022')
pl.legend()
pl.show()

