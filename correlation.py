import readFromDatabase as rfd

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
    tem.corr().to_csv('correlation/'+names[i]+'_cor.csv')