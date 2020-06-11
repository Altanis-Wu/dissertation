import pandas as pd
# list contains the title of useless lines
list = ['\"unweighted base\"', '\"weighted base\"', '\"month\"', '\"base: all respondents\"', '\n', '\"all scotland"']
#open the file and read each line to a list
for i in range(2011, 2020):
    input = []
    output = []
    f = open('original_data/original_visitor/original_visitor_'+str(i)+'.csv', 'r')
    line = f.readline().lower()
    # read each lines to the list
    while line:
        input.append(line)
        line = f.readline().lower()
    # close the file
    f.close()
    for line in input:
        line = line.split(',')
        if line[0] == '\"\"' and line[1] == '\"total\"':
            line[0] = '\"month\"'
            output.append(','.join(x for x in line))
        elif not line[0] == '\"\"' and len(line) > 1 and not list.__contains__(line[0]):
            output.append(','.join(x for x in line))
    f = open('transfer/visitor/visitor_'+str(i)+'.csv', 'w')
    for line in output:
        f.write(line)
    f.close()
for i in range(2011, 2016):
    df = pd.read_csv('transfer/visitor/visitor_'+str(i)+'.csv')
    df.columns = ['month', 'total', 'male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'married', 'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2', 'de', 'employed/self-employed (full or part time)', 'in full or part time education', 'unemployed/not working', '']
    df.to_csv('transfer/visitor/visitor_'+str(i)+'.csv', index = 0)
data = pd.read_csv('transfer/visitor/visitor_2011.csv')
data['year'] = 2011
#Combine and classify the CSV files
for i in range(2012, 2020):
    df = pd.read_csv('transfer/visitor/visitor_'+str(i)+'.csv')
    df['year'] = i
    data = pd.concat([data, df])
#Drop the useless columns
data = data.dropna(axis=1, how="all")
data = data.drop(columns=['total'])
#Drop the useless or repeated rows
data = data.dropna()
data = data[~data.month.isin(['total'])]
#Classify the data based on different types of attributes
gender = data[['year', 'month', 'male', 'female']]
age = data[['year', 'month', '16-24', '25-34', '35-44', '45-54', '55-64', '65+']]
married = data[['year', 'month', 'married', 'not married']]
children = data[['year', 'month', 'yes', 'no']]
cars = data[['year', 'month', 'access to car (1+)',	'no access to car (0)']]
social = data[['year', 'month', 'ab', 'c1', 'c2', 'de']]
working = data[['year', 'month', 'employed/self-employed (full or part time)',	'in full or part time education', 'unemployed/not working']]
#Write each CSV file to the disk
age.to_csv('data/age/age.csv', index=0)
gender.to_csv('data/gender/gender.csv', index=0)
married.to_csv('data/married/married.csv', index=0)
children.to_csv('data/children/children.csv', index=0)
cars.to_csv('data/cars/cars.csv', index=0)
social.to_csv('data/social/social.csv', index=0)
working.to_csv('data/working/working.csv', index=0)