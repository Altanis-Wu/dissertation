from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('Married')
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['Married', 'Not married'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['Married'], marker='o')
plt.plot(overAll['Year'], overAll['Not married'], marker='s')
plt.legend(['Married', 'Not married'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Married Visitors for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/MarriedOverYears.png')
plt.show()