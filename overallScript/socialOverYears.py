from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os
#Read data from database
visitorData = rfd.readFrom('Social')
#Add a column named 'Total'
plt.figure(figsize=(8, 8))
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby('Year')['ab', 'c1', 'c2', 'de'].sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
plt.plot(overAll['Year'], overAll['ab'], marker='o')
plt.plot(overAll['Year'], overAll['c1'], marker='s')
plt.plot(overAll['Year'], overAll['c2'], marker='v')
plt.plot(overAll['Year'], overAll['de'], marker='p')
plt.legend(['AB', 'C1', 'C2', 'DE'])
plt.ylabel('Count(Million)')
plt.xlabel('Years')
plt.title('Number of Visitors from Social Grade for Day Visist in Scotland')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/SocialOverYears.png')
plt.show()