from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'married')
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
married=['married', 'not married']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in married:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o', linewidth=3)
plt.legend(['Married', 'Not married'], fontsize=15)
plt.ylabel('Count(Million)', fontsize=15, weight='bold')
plt.xlabel('Years', fontsize=15, weight='bold')
plt.xlim(2011, 2019)
plt.title('Number of Married Visitors for Day Visit in Scotland', fontsize=15, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/MarriedOverYears.png')
plt.show()