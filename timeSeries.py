import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as ss
import numpy as np
from sklearn.metrics import mean_squared_error

list=[('gender', 'female'), ('cars', 'access to car (1+)'), ('married', 'married'),
      ('working', 'employed/self-employed (full or part time)')]
plt.figure(figsize=(8, 8))
for i in range(len(list)):
    plt.subplot(2, 2, i+1)
    data=rfd.readCertainVisitor('visitor', list[i][0], list[i][1]).groupby('Year').sum().reset_index()
    #print(data.corr())
    #print(data.corr(method='spearman'))
    plt.scatter(data['Year'], data['Count'])
    x=data['Year'].values.reshape(-1, 1)
    y=data['Count'].values.reshape(-1, 1)
    reg=LinearRegression()
    reg.fit(x, y)
    print(list[i])
    print("The linear model is: y = {:.5} + {:.5}x".format(reg.intercept_[0], reg.coef_[0][0]))
    predictions = reg.predict(x)
    kf = ss.chisquare(data['Count'].to_list(), f_exp=predictions.flatten())
    plt.plot(data['Year'], predictions)
    plt.xlabel('Year', fontsize=15)
    plt.ylabel('Count(Million)', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    if i==3:
        plt.title('Number of Visistors in Working', fontsize=15)
    elif i==0:
        plt.title('Number of Female Visitors', fontsize=15)
    elif i==2:
        plt.title('Number of Married Visitors', fontsize=15)
    elif i==1:
        plt.title('Number of Visitors Using Cars', fontsize=15)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    print(kf)
    print(rfd.meanAbsoluteError(data['Count'].to_list(), predictions.flatten()))
    print(np.sqrt(mean_squared_error(data['Count'].to_list(), predictions.flatten())))
plt.savefig('timeSeries/time_series.png')
plt.show()
'''
list=[11.176324024889803, 9.586669689232346, 11.357963048614193, 11.489515213022441, 11.79658440313964, 10.717373750094904, 15.097788546246084, 16.2194101113754, 11.832229699623305, 12.518256656136199, 9.014130148498916, 10.57445154684034, 9.750474692460907, 9.878126693884434, 9.63028389851492, 12.239854455300748, 9.636456662273986, 12.731773782571148, 13.536696803393731, 18.925051252270485, 14.92850921048324, 11.382444980955396, 9.757059622219991, 11.61088045677361, 10.446602500914343, 9.703650362699376, 12.568248882573265, 10.928788941727753, 12.55413310221376, 11.382215382054556, 16.395693841839233, 13.43593218770847, 14.100665827466367, 11.69838861874631, 10.839639859753241, 12.476822707754714, 10.007995247421503, 8.813480459075302, 13.613749114977278, 12.913950433213863, 10.353843857558125, 12.749651331888503, 12.035300346096632, 20.035140210893665, 10.914511373356627, 10.288214116713212, 9.735451655929147, 11.917350135418383, 9.781009620350119, 8.57814626994522, 10.012921975844172, 10.565187066893934, 11.65413260003662, 12.109484918820803, 11.948294894770086, 13.917804170527146, 13.317764325862397, 11.336236249837162, 11.907894559381441, 11.608002552148008, 11.244766773974638, 9.29063763635905, 12.086747650155505, 10.281786869411654, 10.62451114114261, 11.03963936911565, 13.162035460994955, 14.613767882664991, 11.375795029637308, 11.35008153976724, 10.342629941618053, 11.935732456529475]
output=[]
sum=0
for i in range(len(list)):
    if i%12!=0:
        sum+=list[i]
    else:
        output.append(sum)
        sum=list[i]
output.append(sum)
print(output)
'''