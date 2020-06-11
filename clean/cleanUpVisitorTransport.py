import pandas as pd
import os
# list contains the title of useless lines for visitors and activities
list = ['\"unweighted base\"', '\"weighted base\"', '\"activities undertaken\"', '\"base: all respondents\"', '\n',
        '\"all scotland"', '\"none\"', '\"total\"', '', 'unweighted base', 'weighted base', 'activities undertaken',
        'base: all respondents', 'all scotland', 'none', 'total', '\"form of transport used on trip\"']
rows = ['male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+',
                  'married', 'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2',
                  'de', 'employed/self-employed (full or part time)', 'in full or part time education', 'unemployed/not working']
for i in range(2011, 2020):
    input = []
    output = []
    f = open(os.path.dirname(os.getcwd())+'/original_data/original_visitor_transport/original_visitor_transport_' + str(i) + '.csv', 'r')
    line = f.readline().lower()
    # read each lines to the list
    while line:
        input.append(line)
        line = f.readline().lower()
    # close the file
    f.close()
    for line in input:
        line = line.split(',')
        if line[0] == '\"\"' and (line[1] == '\"total\"' or line[1] == 'total'):
            line[0] = '\"transport\"'
            output.append(','.join(x for x in line))
        elif not (line[0] == '\"\"' or line[0] == '\" \"' ) and len(line) > 1 and not list.__contains__(line[0]):
            output.append(','.join(x for x in line))
    f = open(os.path.dirname(os.getcwd())+'/transfer/visitor_transport/visitor_transport_' + str(i) + '.csv', 'w')
    for line in output:
        f.write(line)
    f.close()
for i in range(2011, 2016):
    df = pd.read_csv(os.path.dirname(os.getcwd())+'/transfer/visitor_transport/visitor_transport_' + str(i) + '.csv')
    df.columns = ['transport', 'total', 'male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'married', 'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2', 'de', 'employed/self-employed (full or part time)', 'in full or part time education', 'unemployed/not working', '']
    df.to_csv(os.path.dirname(os.getcwd())+'/transfer/visitor_transport/visitor_transport_' + str(i) + '.csv', index = 0)
data = pd.read_csv(os.path.dirname(os.getcwd())+'/transfer/visitor_transport/visitor_transport_2011.csv')
data['year'] = 2011
#Combine and classify the CSV files
for i in range(2012, 2020):
    df = pd.read_csv(os.path.dirname(os.getcwd())+'/transfer/visitor_transport/visitor_transport_'+str(i)+'.csv')
    df.columns = ['transport', 'total', 'male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'married',
                  'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2', 'de',
                  'employed/self-employed (full or part time)', 'in full or part time education',
                  'unemployed/not working', '']
    df['year'] = i
    data = pd.concat([data, df])
data = data.dropna(axis=1, how="all")
data = data.drop(columns=['total'])
for i in rows:
    data[i] = data[i].apply(lambda x:0.0 if x=='-' else x)
gender = data[['year', 'transport', 'male', 'female']]
age = data[['year', 'transport', '16-24', '25-34', '35-44', '45-54', '55-64', '65+']]
married = data[['year', 'transport', 'married', 'not married']]
children = data[['year', 'transport', 'yes', 'no']]
cars = data[['year', 'transport', 'access to car (1+)',	'no access to car (0)']]
social = data[['year', 'transport', 'ab', 'c1', 'c2', 'de']]
working = data[['year', 'transport', 'employed/self-employed (full or part time)',	'in full or part time education', 'unemployed/not working']]
#Write each CSV file to the disk
age.to_csv(os.path.dirname(os.getcwd())+'/data/age/age_transport.csv', index=0)
gender.to_csv(os.path.dirname(os.getcwd())+'/data/gender/gender_transport.csv', index=0)
married.to_csv(os.path.dirname(os.getcwd())+'/data/married/married_transport.csv', index=0)
children.to_csv(os.path.dirname(os.getcwd())+'/data/children/children_transport.csv', index=0)
cars.to_csv(os.path.dirname(os.getcwd())+'/data/cars/cars_transport.csv', index=0)
social.to_csv(os.path.dirname(os.getcwd())+'/data/social/social_transport.csv', index=0)
working.to_csv(os.path.dirname(os.getcwd())+'/data/working/working_transport.csv', index=0)