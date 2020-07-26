import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

age=['16-24', '25-34', '35-44', '45-54', '55-64', '65+']
cars=['access to car (1+)', 'no access to car (0)']
children=['yes', 'no']
gender=['male', 'female']
married=['married', 'not married']
social=['ab', 'c1', 'c2', 'de']
working=['employed/self-employed (full or part time)',
         'in full or part time education', 'unemployed/not working']
ageData=rfd.readFrom('visitor', 'age')
total=ageData.groupby('Year').sum().reset_index()['Count']
attributes=[age, gender, cars, children, married, social, working]
names=['age', 'gender', 'cars', 'children', 'married', 'social', 'working']

for i in range(len(names)):
    data = rfd.readFrom('visitor', names[i])
    tem = data.groupby(['Year', 'Attribute']).sum().reset_index()
    plt.figure(figsize=(8, 8))
    for item in attributes[i]:
        x = tem[tem['Attribute'] == item]['Count'].values.reshape(-1, 1)
        y = total.values.reshape(-1, 1)
        reg = LinearRegression()
        reg.fit(x, y)
        print(item)
        print("The linear model is: y = {:.5} + {:.5}x".format(reg.intercept_[0], reg.coef_[0][0]))
        predictions = reg.predict(x)
        x = tem[tem['Attribute'] == item]['Count']
        y = total.values.reshape(-1, 1)
        x2 = sm.add_constant(x)
        est = sm.OLS(y, x2)
        est2 = est.fit()
        print(est2.summary())
        plt.scatter(tem[tem['Attribute'] == item]['Count'], total)
        plt.plot(tem[tem['Attribute'] == item]['Count'], predictions)
    plt.legend(attributes[i])
    plt.xlabel('Number of Visitors in Different Category')
    plt.ylabel('Number of total ')
    plt.title(names[i]+' and total number of visitors')
    plt.savefig('scatter/'+names[i]+'and total number of visitors.png')
    plt.show()