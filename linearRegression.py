import readFromDatabase as rfd
import matplotlib.pyplot as plt

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
        plt.scatter(tem[tem['Attribute'] == item]['Count'], total)
    plt.legend(attributes[i])
    plt.xlabel('Number of Visitors in Different Category')
    plt.ylabel('Number of total ')
    plt.title(names[i]+' and total number of visitors')
    plt.savefig('scatter/'+names[i]+'and total number of visitors.png')
    plt.show()