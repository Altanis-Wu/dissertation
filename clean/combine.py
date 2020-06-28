import pandas as pd
import os

type=['_place', '_transport']
attributes = ['age', 'cars', 'children', 'gender', 'married', 'social', 'working']
for x in attributes:
    data = pd.read_csv(os.path.dirname(os.getcwd()) + '/data/' + x + '/' + x + '_activity.csv')
    for y in type:
        df = pd.read_csv(os.path.dirname(os.getcwd()) + '/data/' + x + '/' + x + y+'.csv')
        data = pd.concat([data, df])
    data.to_csv(os.path.dirname(os.getcwd()) + '/data/' + x + '/' + x+'_combine.csv')