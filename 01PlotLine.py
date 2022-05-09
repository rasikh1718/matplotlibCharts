#pip install matplotlib

from matplotlib import pyplot

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
mobsold=[37,16,22,56,45,125,89,77,82,48,55,71]

pyplot.plot(months,mobsold,color='red',linestyle='dashdot')
pyplot.xlabel('Month')
pyplot.ylabel('Sold')
pyplot.title('Mobile sale in 2021')
pyplot.grid()
pyplot.show()
