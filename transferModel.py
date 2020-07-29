import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as ss
import numpy as np
import statsmodels.api as sm

ageData=rfd.readFrom('visitor', 'age')
total=ageData.groupby('Year').sum().reset_index()
list=[('married', 'married'), ('gender', 'female')]
plt.figure(figsize=(8, 8))
plt.plot(total['Year'], total['Count'], marker='o')
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
    #Both of them Chi-square about 0.982
    plt.plot(range(2011, 2021), predictions, marker='o')
    kf=ss.chisquare(total['Count'].to_list(), f_exp=predictions[:-1].flatten())
    print(kf)
plt.legend(['Actual value', 'Prediction value based on married visitor', 'Prediction value based on female visitor'])
plt.xlabel('Year')
plt.ylabel('Number of Visitors(Million)')
plt.title('Total Number of Visitors Over years')
plt.savefig('figures/predictionTransferModel.png')
plt.show()