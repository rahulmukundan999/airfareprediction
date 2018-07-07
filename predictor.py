from pandas import read_csv
import time
import pandas as pd
import sys
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
d=sys.argv[4]
e=sys.argv[5]

j=d+'-'+e+'.csv'

def parser(x):
	return datetime.strptime(x, '%b %Y')

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

def month_name(month_num):
    switcher = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December",
        }
    return switcher.get(month_num, "Invalid Month Value")
series = read_csv(j, parse_dates=[0], squeeze=True, date_parser=parser)

#print(series)
#print(len(series))
lastDate = series['year'][len(series)-1]
lastMonth = 'January'
#lastDate.month
#lastDate.year
if(lastDate.year == 2018):
    lastMonth = month_name(lastDate.month % 12)
    #print(lastMonth)


series = read_csv(j, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

X = series.values
size = int(len(X)-12)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

#end_index = pd.datetime(2018,7,25)
for t in range(len(test)):
	model = ARIMA(history, order=(a,b,c))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	#print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
month_num = predictions.index(min(predictions))
month_num = (month_num + lastDate.month)%12
optimal_month = month_name(month_num)

# plot
fig = pyplot.figure(figsize=(9,7))
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Airfare Predictor Projection \n Prediction starts from %s-2018'%(lastMonth))

ax.set_xlabel('Month of Year\n\n Lowest Price = %.3f                    Average Price = %.3f                      Cheapest Month to Travel = %s' % (min(predictions),Average(predictions),optimal_month))
ax.set_ylabel('Price($)')

ax.plot(predictions, color='red')

pyplot.savefig('fig.png')