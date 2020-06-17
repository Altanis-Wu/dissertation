from matplotlib import pyplot as plt
import readFromDatabase as rfd
#Read data from database
visitorData = rfd.readFrom('Working')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['employed/self-employed (full or part time)',
                                      'in full or part time education',
                                      'unemployed/not working'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['employed/self-employed (full or part time)'], marker='o')
plt.plot(overAll['Year'], overAll['in full or part time education'], marker='s')
plt.plot(overAll['Year'], overAll['unemployed/not working'], marker='v')
plt.legend(['Employed/self-employed (full or part time)',
                                      'In full or part time education',
                                      'Unemployed/not working'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors from Different Working Status for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig('figures/WorkingOverYears.png')
plt.show()