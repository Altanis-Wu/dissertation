import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm

ageData=rfd.readFrom('visitor', 'age')
total=ageData.groupby('Year').sum().reset_index()
data=rfd.readCertainVisitor('visitor', 'married', 'married').groupby('Year').sum().reset_index()
x=data['Year'].values.reshape(-1, 1)
y=data['Count'].values.reshape(-1, 1)
reg1=LinearRegression()
#The linear regression on 'married' based on time series
reg1.fit(x, y)
x=np.r_[x, [[2020]]]
predictions = reg1.predict(x)
#The linear regression between married visitors and total number of visitors.
x=data['Count'].values.reshape(-1, 1)
y=total['Count'].values.reshape(-1, 1)
reg2=LinearRegression()
reg2.fit(x, y)
predictions = reg2.predict(predictions)
#Number of visitors for next year is 133.579 million.
print(predictions)
plt.figure(figsize=(8, 8))
plt.plot(total['Year'], total['Count'], marker='o')
plt.plot(range(2011, 2021), predictions, marker='o')
plt.legend(['Actual value', 'Prediction value'])
plt.xlabel('Year')
plt.ylabel('Number of Visitors(Million)')
plt.title('Total Number of Visitors Over years')
plt.savefig('figures/predictionTransferModel.png')
plt.show()
#The performance of the model and R-squared is about 0.715
x2=sm.add_constant(data['Year'])
est=sm.OLS(data['Count'], x2)
est2=est.fit()
print(est2.summary())