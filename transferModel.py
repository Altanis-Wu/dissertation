import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as ss
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error

ageData=rfd.readFrom('visitor', 'age')
total=ageData.groupby('Year').sum().reset_index()
list=[('gender', 'female'), ('cars', 'access to car (1+)'), ('married', 'married'),
      ('working', 'employed/self-employed (full or part time)')]
plt.figure(figsize=(8, 8))
plt.plot(total['Year'], total['Count'], marker='o')
ARIMA=[141.4, 144.0, 146.5, 143.4, 136.7, 137.3]
for i in list:
    data = rfd.readCertainVisitor('visitor', i[0], i[1]).groupby('Year').sum().reset_index()
    x = data['Year'].values.reshape(-1, 1)
    y = data['Count'].values.reshape(-1, 1)
    reg1 = LinearRegression()
    # The linear regression on 'married' based on time series
    reg1.fit(x, y)
    x = np.r_[x, [[2020]]]
    predictions = reg1.predict(x)
    # The linear regression between married visitors and total number of visitors.
    x = data['Count'].values.reshape(-1, 1)
    y = total['Count'].values.reshape(-1, 1)
    reg2 = LinearRegression()
    reg2.fit(x, y)
    predictions = reg2.predict(predictions)
    # Number of visitors for next year is 133.579 million for married visitors and 135.277 million for female visitor.
    #Chi-square for female visitor is 1.925, and for married visitor is 1.969
    #MSE for female visitors is 4.386, and for married visitor is 4.462
    plt.plot(range(2011, 2021), predictions, marker='o')
    kf=ss.chisquare(total['Count'].to_list(), f_exp=predictions[:-1].flatten())
    print(i)
    print(kf)
    print(rfd.meanAbsoluteError(total['Count'].to_list(), predictions[:-1].flatten()))
    print(np.sqrt(mean_squared_error(total['Count'].to_list(), predictions[:-1].flatten())))
plt.legend(['Actual value', 'Model basd on female visitor', 'Model basd on visitor using cars',
            'Model basd on married visitor', 'Model basd on working visitor'], fontsize=12)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Number of Visitors(Million)', fontsize=15)
plt.title('Total Number of Visitors Over years', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('figures/predictionTransferModel.png')
plt.show()
print(ss.chisquare(total['Count'].to_list()[3:], f_exp=ARIMA))
print(rfd.meanAbsoluteError(total['Count'].to_list()[3:], ARIMA))
print(np.sqrt(mean_squared_error(total['Count'].to_list()[3:], ARIMA)))