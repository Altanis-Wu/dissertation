import pandas as pd
from sqlalchemy import create_engine
#List of name of tables which
inputFile = ['age', 'cars', 'children', 'gender', 'social', 'working', 'married']
#Connect to MySQL database
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")
#Read each file as dataframe and write them to database
age=['16-24', '25-34', '35-44', '45-54', '55-64', '65+']
cars=['access to car (1+)', 'no access to car (0)']
children=['yes', 'no']
gender=['male', 'female']
married=['married', 'not married']
social=['ab', 'c1', 'c2', 'de']
working=['employed/self-employed (full or part time)', 'in full or part time education', 'unemployed/not working']
columns=[age, cars, children, gender, social, working, married]

for i in range(len(inputFile)):
    input = pd.read_csv("data/"+inputFile[i]+"/"+inputFile[i]+".csv")
    input['type']=inputFile[i]
    for index, row in input.iterrows():
        for item in columns[i]:
            sql = "insert into visitor values (" + str(row.year) + ", " + str(row.month) + ", \"" \
                  + row.type + "\", \"" + item + "\", " + str(row[item]) + ");"
            connection.execute(sql)



#Read each file about attributes and actions as dataframe and write them to database
"""
for file in inputFile:
    input = pd.read_csv("data/"+file.lower()+'/'+file.lower()+"_action.csv")
    input.to_sql(file.lower()+"_action", connection, schema='DissertationDatabase', if_exists='append', index=False)
"""