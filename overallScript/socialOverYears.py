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
    plt.plot(data['Year'], data['Count'], marker='o')
plt.legend(['AB', 'C1', 'C2', 'DE'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors from Social Grade for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/SocialOverYears.png')
plt.show()