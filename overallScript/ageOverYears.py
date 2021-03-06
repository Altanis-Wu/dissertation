from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'age')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
age=['16-24', '25-34', '35-44', '45-54', '55-64', '65+']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in age:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o', linewidth=3)
plt.legend(['16-24', '25-34', '35-44', '45-54', '55-64', '65+'], fontsize=12)
plt.ylabel('Count(Million)', fontsize=12, weight='bold')
plt.xlabel('Years', fontsize=12, weight='bold')
plt.xlim(2011, 2019)
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.title('Number of Visitors from Different Age for Day Visit in Scotland', fontsize=15, weight='bold')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/AgeOverYears.png')
plt.show()
