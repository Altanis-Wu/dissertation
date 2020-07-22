import readFromDatabase as rfd

ageData=rfd.readFrom('visitor', 'age')
genderData=rfd.readFrom('visitor', 'gender')
carsData=rfd.readFrom('visitor', 'cars')
childrenData=rfd.readFrom('visitor', 'children')
marriedData=rfd.readFrom('visitor', 'married')
socialData=rfd.readFrom('visitor', 'social')
workingData=rfd.readFrom('visitor', 'working')
total=ageData.groupby('Year').sum().reset_index()['Count']
print(total)
