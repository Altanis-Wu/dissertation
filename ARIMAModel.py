import readFromDatabase as rfd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import scipy.stats as ss
from sklearn.metrics import mean_squared_error
#The function to make a Dickey-Fuller test
def teststationarity(ts):
    dftest = adfuller(ts)
    #Describe the result
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    return dfoutput
#The function to draw the figures about auto-correlation and partial auto-correlation.
def draw_acf_pacf(ts,lags):
    f = plt.figure(facecolor='white')
    ax1 = f.add_subplot(2, 1, 1)
    plot_acf(ts,ax=ax1,lags=lags)
    ax2 = f.add_subplot(2, 1, 2)
    plot_pacf(ts,ax=ax2,lags=lags)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
#Generate the date for index
date=[]
for i in range(2011, 2020):
    for j in range(1, 13):
        date.append(str(i)+'-'+str(j))
#Read the data from database and set the date as index.
timeData=rfd.readFrom('visitor', 'age').groupby(['Year', 'Month']).sum().reset_index()
timeData['date']=date
timeData=timeData.set_index(pd.to_datetime(timeData['date'], format='%Y-%m'))
timeData=timeData.drop(columns=['Year', 'Month', 'date'])
#To reduce the data fluctuation range, make logarithm operation
tsLog=np.log(timeData)
#Make decomposition to original data
decomposition=seasonal_decompose(tsLog)
trend=decomposition.trend
seasonal=decomposition.seasonal
residual=decomposition.resid
#Draw the figures about the trend, periodicity and residual of the data.
plt.figure(figsize=(8, 8))
plt.subplot(3, 1, 1)
trend.plot()
plt.title('The Trend of Data')
plt.subplot(3, 1, 2)
plt.subplots_adjust(hspace=0.5)
seasonal.plot()
plt.subplots_adjust(hspace=0.5)
plt.title('The Periodicity of Data')
plt.subplot(3, 1, 3)
plt.subplots_adjust(hspace=0.5)
residual.plot()
plt.title('The Residual of Data')
plt.savefig('figures/composition')
plt.show()
#Calculate the means, standard devitation for data. As the periodicity is a year, the size of rolling window is 12.
residual.dropna(inplace=True)
rollMeanRes=residual.rolling(window=12).mean()
rollStdRes=residual.rolling(window=12).std()
plt.figure(figsize=(8, 8))
residual.plot(label='Residual')
rollMeanRes.plot(label='Rolling Mean')
rollStdRes.plot(label='Rolling Standard Devitation')
plt.title('Rolling Mean & Standard Deviation')
plt.savefig('figures/mean&stdResidual.png')
plt.show()
print(teststationarity(residual))
draw_acf_pacf(tsLog, 30)
#Build the ARIMA model
model = ARIMA(tsLog, order=(36, 0, 5))
resultArima = model.fit( disp=-1, method='css')
predictTs = resultArima.predict()
predict=np.exp(predictTs).reset_index()
predict.columns=['date', 'Count']
predict=predict.set_index(predict['date']).drop(columns=['date'])
timeData=timeData.iloc[36:]
plt.figure(figsize=(8, 8))
plt.plot(timeData)
plt.plot(predict)
plt.legend(['Actual', 'Predict'])
plt.title('The Actual Values and the Predict Values')
plt.xlabel('Date')
plt.ylabel('Number of Visitors(Million)')
plt.savefig('figures/ARIMA.png')
plt.show()
#Chi_square=0.80, MAE=3.8
print(rfd.meanAbsoluteError(predict['Count'].to_list(), timeData['Count'].to_list()))
print(ss.chisquare(timeData['Count'].to_list(), f_exp=predict['Count'].to_list()))
print(np.sqrt(mean_squared_error(timeData['Count'].to_list(), predict['Count'].to_list())))
print(predict['Count'].to_list())