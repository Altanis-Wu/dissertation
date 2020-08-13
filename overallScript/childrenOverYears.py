from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'children')
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
children=['yes', 'no']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in children:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o')
plt.legend(['Yes', 'No'], fontsize=15)
plt.ylabel('Count(Million)', fontsize=15)
plt.xlabel('Years', fontsize=15)
plt.xlim(2011, 2019)
plt.title('Number of Visitors who Have Children for Day Visist in Scotland', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/ChildrenOverYears.png')
plt.show()