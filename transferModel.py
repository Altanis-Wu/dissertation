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
    plt.plot(range(2011, 2021), predictions, marker='o', linewidth=3)
    kf=ss.chisquare(total['Count'].to_list(), f_exp=predictions[:-1].flatten())
    print(i)
    print(kf)
    print(rfd.meanAbsoluteError(total['Count'].to_list(), predictions[:-1].flatten()))
    print(np.sqrt(mean_squared_error(total['Count'].to_list(), predictions[:-1].flatten())))
plt.legend(['Actual value', 'Model basd on female visitor', 'Model basd on visitor using cars',
            'Model basd on married visitor', 'Model basd on working visitor'], fontsize=12)
plt.xlabel('Year', fontsize=15, weight='bold')
plt.ylabel('Number of Visitors(Million)', fontsize=15, weight='bold')
plt.title('Total Number of Visitors Over years', fontsize=15, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.savefig('figures/predictionTransferModel.png')
plt.show()
print(ss.chisquare(total['Count'].to_list()[3:], f_exp=ARIMA))
print(rfd.meanAbsoluteError(total['Count'].to_list()[3:], ARIMA))
print(np.sqrt(mean_squared_error(total['Count'].to_list()[3:], ARIMA)))
list1=[1.0228658, 1.1495133, 1.1585621, 1.1338144, 1.0090715, 0.8064170, 0.8748701, 0.9036134, 1.1835352, 1.3982503, 1.3128365,
1.2302274, 0.9905240, 0.9680694, 1.0620318, 1.1832700, 1.2828081, 1.2877447, 1.1372988, 1.0609163, 0.9923317, 1.1147535,
1.1708905, 1.3132853, 1.2184974, 1.1252307, 0.9252025, 0.8061855, 0.8876209, 0.9881224, 1.1731545, 1.3107270, 1.1726009,
1.0021387, 1.0288463, 1.0113366, 1.2153016, 1.2890119, 1.1727759, 0.8185130, 0.6298551, 0.2186260]
list2=[1.11, 1.19, 1.20, 1.12, 0.95, 0.89, 0.90, 1.08, 1.32, 1.39, 1.34, 1.16, 1.04, 1.05, 1.15, 1.27, 1.33, 1.26, 1.16, 1.07, 1.10, 1.17,
1.29, 1.30, 1.23, 1.07, 0.91, 0.88, 0.95, 1.11, 1.28, 1.28, 1.15, 1.08, 1.05, 1.16, 1.28, 1.27, 1.04, 0.78, 0.40, 0.18]
print(ss.chisquare(list2, list1))