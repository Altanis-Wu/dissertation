from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('visitor', 'working')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year', 'Attribute']).sum().reset_index()
working=['employed/self-employed (full or part time)',
         'in full or part time education', 'unemployed/not working']
#Draw a line chart to show the overall trend and set labels and titles for the chart.
for x in working:
    data=overAll[overAll['Attribute']==x]
    plt.plot(data['Year'], data['Count'], marker='o', linewidth=3)
plt.legend(['Employed/self-employed (full or part time)',
                                      'In full or part time education',
                                      'Unemployed/not working'], fontsize=12)
plt.ylabel('Count(Million)', fontsize=15, weight='bold')
plt.xlabel('Years', fontsize=15, weight='bold')
plt.xlim(2011, 2019)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Number of Visitors from Different Working Status', fontsize=15, weight='bold')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/WorkingOverYears.png')
plt.show()