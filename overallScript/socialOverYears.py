from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'social')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
social=['ab', 'c1', 'c2', 'de']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in social:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o', linewidth=3)
plt.legend(['AB', 'C1', 'C2', 'DE'], fontsize=15)
plt.ylabel('Count(Million)', fontsize=15, weight='bold')
plt.xlabel('Years', fontsize=15, weight='bold')
plt.xlim(2011, 2019)
plt.title('Number of Visitors from Social Grade for Day Visit in Scotland', fontsize=15, weight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/SocialOverYears.png')
plt.show()