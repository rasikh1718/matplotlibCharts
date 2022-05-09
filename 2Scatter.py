from matplotlib import pyplot

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
mobsold=[37,16,22,56,45,125,89,77,82,48,55,71]

pyplot.scatter(months,mobsold,color='red')
pyplot.xlabel('months')
pyplot.ylabel('sold')
pyplot.title('number of sold in month')
pyplot.show()