from matplotlib import pyplot as plt
import readFromDatabase as rfd
import math
import os
#Read data from database
date=[]
for i in range(2011, 2020):
    for j in range(1, 13):
        date.append(str(i)+'-'+str(j))
visitorData = rfd.readFrom('visitor', 'age')
plt.figure(figsize=(8, 8))
ax=plt.gca()
#Group the data based on 'Year', calculate the number of visitors for each year and generate a new dataframe.
overAll = visitorData.groupby(['Year']).sum().reset_index()
#Draw a line chart to show the overall trend and set labels and titles for the chart.
#overAll['Count']=overAll['Count'].apply(lambda x: math.log(x, 10))
plt.plot(overAll['Year'], overAll['Count'], marker='o', linewidth=3)
plt.xlim(2011, 2019)
plt.ylabel('Count(Million)', fontsize=15, weight='bold')
plt.xlabel('Times', fontsize=15, weight='bold')
#plt.xticks(range(len(date))[::3], date[::3], rotation=90)
plt.title('Number of Visitors for Day Visit in Scotland', fontsize=15, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
#Save the chart as a 'PNG' file.
plt.savefig(os.path.dirname(os.getcwd())+'/figures/overall.png')
plt.show()