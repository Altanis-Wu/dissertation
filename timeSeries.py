import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as ss

list=[('gender', 'female'), ('cars', 'access to car (1+)'), ('married', 'married'),
      ('working', 'employed/self-employed (full or part time)')]
for item in list:
    plt.figure(figsize=(8, 8))
    data=rfd.readCertainVisitor('visitor', item[0], item[1]).groupby('Year').sum().reset_index()
    print(data.corr())
    print(data.corr(method='spearman'))
    plt.scatter(data['Year'], data['Count'])
    x=data['Year'].values.reshape(-1, 1)
    y=data['Count'].values.reshape(-1, 1)
    reg=LinearRegression()
    reg.fit(x, y)
    print(item)
    print("The linear model is: y = {:.5} + {:.5}x".format(reg.intercept_[0], reg.coef_[0][0]))
    predictions = reg.predict(x)
    kf = ss.chisquare(data['Count'].to_list(), f_exp=predictions.flatten())
    print(kf)
    plt.plot(data['Year'], predictions)
    plt.xlabel('Year')
    plt.ylabel('Number of Visitors')
    plt.title('Number of visistors in '+item[1])
    plt.savefig('timeSeries/'+item[0]+'_time_series.png')
    plt.show()
