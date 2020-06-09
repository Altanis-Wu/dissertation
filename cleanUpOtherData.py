import pandas as pd
# list contains the title of useless lines for visitors and activities
list = ['\"unweighted base\"', '\"weighted base\"', '\"activities undertaken\"', '\"base: all respondents\"', '\n', '\"all scotland"', '\"none\"', '\"total\"', '', 'unweighted base', 'weighted base', 'activities undertaken', 'base: all respondents', 'all scotland', 'none', 'total']
columns = ['visited friends or family for leisure',	'\'special\' shopping for items that you do not regularly buy',	'went out for a meal', 'went on a night out to a bar, pub and/or club', 'went out for entertainment – to a cinema, concert or theatre', 'undertook outdoor leisure activities such as walking, cycling, golf, etc.', 'took part in other leisure activities such as hobbies, evening classes, etc. (outside of your home)',	'took part in sports, including exercise classes, going to the gym', 'watched live sporting event (not on tv)', 'went to visitor attractions such as a historic house, garden, theme park, museum, zoo, etc.', 'went to a special public event such as a festival, exhibition, etc.', 'went to a special event of a personal nature such as a wedding, graduation, christening, etc.', 'went on days out to a beauty/health centre/spa, etc.', 'went on general days out/ to explore an area', 'went on day trips/excursions for another leisure purpose not mentioned above']
for i in range(2011, 2020):
    input = []
    output = []
    f = open('original_data/original_visitor_activity/original_visitor_activity_' + str(i) + '.csv', 'r')
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
            line[0] = '\"activity\"'
            output.append(','.join(x for x in line))
        elif not (line[0] == '\"\"' or line[0] == '\" \"' ) and len(line) > 1 and not list.__contains__(line[0]):
            output.append(','.join(x for x in line))
    f = open('transfer/visitor_activity/visitor_activity_' + str(i) + '.csv', 'w')
    for line in output:
        f.write(line)
    f.close()
for i in range(2011, 2016):
    df = pd.read_csv('transfer/visitor_activity/visitor_activity_'+str(i)+'.csv')
    df.columns = ['activity', 'total', 'male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'married', 'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2', 'de', 'employed/self-employed (full or part time)', 'in full or part time education', 'unemployed/not working', '']
    df.to_csv('transfer/visitor_activity/visitor_activity_'+str(i)+'.csv', index = 0)
data = pd.read_csv('transfer/visitor_activity/visitor_activity_2011.csv')
data['year'] = 2011
data['activity'] = columns
#Combine and classify the CSV files
for i in range(2012, 2020):
    df = pd.read_csv('transfer/visitor_activity/visitor_activity_'+str(i)+'.csv')
    df.columns = ['activity', 'total', 'male', 'female', '16-24', '25-34', '35-44', '45-54', '55-64', '65+', 'married',
                  'not married', 'yes', 'no', 'access to car (1+)', 'no access to car (0)', 'ab', 'c1', 'c2', 'de',
                  'employed/self-employed (full or part time)', 'in full or part time education',
                  'unemployed/not working', '']
    df['year'] = i
    df['activity'] = columns
    data = pd.concat([data, df])
data = data.dropna(axis=1, how="all")
data = data.drop(columns=['total'])
data.to_csv('tem.csv', index=0)
gender = data[['year', 'activity', 'male', 'female']]
age = data[['year', 'activity', '16-24', '25-34', '35-44', '45-54', '55-64', '65+']]
print(age)
married = data[['year', 'activity', 'married', 'not married']]
children = data[['year', 'activity', 'yes', 'no']]
cars = data[['year', 'activity', 'access to car (1+)',	'no access to car (0)']]
social = data[['year', 'activity', 'ab', 'c1', 'c2', 'de']]
working = data[['year', 'activity', 'employed/self-employed (full or part time)',	'in full or part time education', 'unemployed/not working']]
#Write each CSV file to the disk
age.to_csv('data/age_activity.csv', index=0)
gender.to_csv('data/gender_activity.csv', index=0)
married.to_csv('data/married_activity.csv', index=0)
children.to_csv('data/children_activity.csv', index=0)
cars.to_csv('data/cars_activity.csv', index=0)
social.to_csv('data/social_activity.csv', index=0)
working.to_csv('data/working_activity.csv', index=0)