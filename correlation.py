import readFromDatabase as rfd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ageData=rfd.readFrom('visitor', 'age')
genderData=rfd.readFrom('visitor', 'gender')
carsData=rfd.readFrom('visitor', 'cars')
childrenData=rfd.readFrom('visitor', 'children')
marriedData=rfd.readFrom('visitor', 'married')
socialData=rfd.readFrom('visitor', 'social')
workingData=rfd.readFrom('visitor', 'working')
total=ageData.groupby('Year').sum().reset_index()['Count']
Data=[ageData, genderData, carsData, childrenData, marriedData, socialData, workingData]
names=['age', 'gender', 'cars', 'children', 'married', 'social', 'working']
for i in range(len(Data)):
    tem=Data[i].groupby(['Year', 'Attribute']).sum().reset_index()
    tem=tem.pivot(index='Year', columns='Attribute', values='Count').reset_index().drop(columns=['Year'])
    tem['total']=total
    #tem.corr().to_csv('correlation/'+names[i]+'_cor.csv')
    #tem.corr(method='spearman').to_csv('correlation/'+names[i]+'_spearman.csv')
listPearson=np.array([[0.383, 0.52, 0.143, 0.815, 0.168, 0.408, 0.911, 0.207, 0.946, -0.083,
             0.914, 0.745, 0.893, 0.201, 0.679, 0.803, 0.424, -0.505, 0.954, -0.236, 0.497],
             [0.502, 0.35, 0.167, 0.9, 0.067, 0.1, 0.817, 0.45, 0.867, -0.008, 0.767, 0.767, 0.75, 0.3,
              0.667, 0.783, 0.5, -0.460, 0.983, 0.016, 0.383]])
listPearson=listPearson.T
ax=sns.heatmap(listPearson, cmap='YlGnBu')
plt.title('Correlation of Different Factors in Tourism')
ax.set_xticklabels(['Pearson', 'Spearman'])
attributes=['16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'access to car (1+)', 'no access to car (0)', 'no children',
            'have children', 'female', 'male', 'married', 'not married', 'social(ab)', 'social(c1)', 'social(c2)',
            'social(de)', 'working', 'in education', 'not working']
ax.set_yticklabels(attributes)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()