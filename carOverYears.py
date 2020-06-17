from matplotlib import pyplot as plt
import readFromDatabase as rfd
#Read data from database
visitorData = rfd.readFrom('Cars')
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['access to car (1+)', 'no access to car (0)'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['access to car (1+)'], marker='o')
plt.plot(overAll['Year'], overAll['no access to car (0)'], marker='s')
plt.legend(['Access to car (1+)', 'No access to car (0)'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors who Have Cars for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig('figures/CarOverYears.png')
plt.show()