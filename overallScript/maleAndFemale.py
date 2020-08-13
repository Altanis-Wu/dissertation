from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'gender')
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
gender=['male', 'female']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in gender:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o')
plt.legend(['Male', 'Female'], fontsize=15)
plt.ylabel('Count(Million)', fontsize=15)
plt.xlabel('Years', fontsize=15)
plt.xlim(2011, 2019)
plt.title('Number of Visitors from Different Genders for Day Visist in Scotland', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/GenderOverYears.png')
plt.show()