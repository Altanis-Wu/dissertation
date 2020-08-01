import readFromDatabase as rfd
import matplotlib.pyplot as plt
import math

timeData=rfd.readFrom('visitor', 'age').groupby(['Year', 'Month']).sum().reset_index()
timeData['Count']=timeData['Count'].apply(lambda x:math.log(x))
rollMean=timeData['Count'].rolling(window=12).mean()
plt.plot(range(len(timeData['Count'])), timeData['Count'])
rollMean.plot()
rollStd=timeData['Count'].rolling(window=12).std()
rollStd.plot()
plt.legend(['Original', 'Rolling Mean', 'Rolling Standard Devitation'], loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()