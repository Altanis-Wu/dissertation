from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('Age')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['16-24', '25-34', '35-44', '45-54', '55-64', '65+'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['16-24'], marker='o')
plt.plot(overAll['Year'], overAll['25-34'], marker='s')
plt.plot(overAll['Year'], overAll['35-44'], marker='v')
plt.plot(overAll['Year'], overAll['45-54'], marker='p')
plt.plot(overAll['Year'], overAll['55-64'], marker='+')
plt.plot(overAll['Year'], overAll['65+'], marker='x')
plt.legend(['16-24', '25-34', '35-44', '45-54', '55-64', '65+'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors from Different Age for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/AgeOverYears.png')
plt.show()