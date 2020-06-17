from matplotlib import pyplot as plt
import readFromDatabase as rfd
#Read data from database
visitorData = rfd.readFrom('Gender')
#Add a column named 'Total'
visitorData['Total'] = visitorData.Male + visitorData.Female
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['Male', 'Female'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['Male'], marker='o')
plt.plot(overAll['Year'], overAll['Female'], marker='s')
plt.legend(['Male', 'Female'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors from Different Genders for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig('figures/GenderOverYears.png')
plt.show()