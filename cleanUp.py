import pandas as pd
#open the file and read each line to a list
for i in range(2006, 2020):
    f = open('original_data/original_attributes_'+str(i)+'.csv', 'r')
    # list contains the title of useless lines
    list = ['\"unweighted base\"', '\" start month of trip\"', '\"total\"', '\"weighted base\"']
    docs = range(2006, 2020)
    line = f.readline().lower()
    input = []
    # read each lines to the list
    while line:
        input.append(line)
        line = f.readline().lower()
    # close the file
    f.close()
    output = []
    # For each line in the list, check if it is useless. If not, add it to the output list
    for item in input:
        item = item.split(',')
        if item[0] == '\"\"' and item[1] == '\"total\"':
            item[0] = '\"month\"'
            output.append(','.join(x for x in item))
        elif not item[0] == '\"\"' and len(item) > 1 and not list.__contains__(item[0]):
            output.append(','.join(x for x in item))
    # Open another file to write the output list to CSV file.
    f = open('data/visitor_attributes_'+str(i)+'.csv', 'w')
    for item in output:
        f.write(item)
    f.close()
    # Read the new CSV file
    data = pd.read_csv('data/visitor_attributes_'+str(i)+'.csv')
    # Drop all columns which all values in column are null
    data = data.dropna(axis=1, how="all")
    #Drop the repeated range
    if i in range(2016, 2020):
        data = data.drop(columns=['55+', '16-34', '35-54'])
        data['year'] = data['month'].apply(lambda x: x.split('-')[1])
        data['month'] = data['month'].apply(lambda x:x.split('-')[0])
    else:
        data['year'] = data['month'].apply(lambda x: x.split()[1])
        data['month'] = data['month'].apply(lambda x: x.split()[0])
    gender = data[['year', 'month', 'male', 'female']]
    #Classify these data based on gender, children, marrial, working, social grade and so on
    gender.to_csv('data/gender/gender_'+str(i)+'.csv', index=0)
    age = data[['year', 'month', '16-24', '25-34', '35-44', '45-54', '55-64', '65+']]
    age.to_csv('data/age/age_'+str(i)+'.csv', index=0)
    social = data[['year', 'month', 'a', 'b', 'c1', 'c2', 'd', 'e']]
    social.to_csv('data/social_class/social_'+str(i)+'.csv', index=0)
    if i in range(2016, 2020):
        marry = data[['year', 'month', 'married', 'single', 'separated/widowed/divorced']]
        marry.to_csv('data/marital/marry_'+str(i)+'.csv', index=0)
        work = data[['year', 'month', 'full time', 'part time', 'other']]
        work.to_csv('data/working/work_'+str(i)+'.csv', index=0)
    else:
        chilren = data[['year', 'month', 'yes', 'no']]
        chilren.to_csv('data/children/chilren_'+str(i)+'.csv', index=0)