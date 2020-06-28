import pandas as pd
from sqlalchemy import create_engine
#List of name of tables which
inputFile = ['Age', 'Cars', 'Children', 'Gender', 'Married', 'Social', 'Working']
#Connect to MySQL database
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")
#Read each file as dataframe and write them to database
"""
for file in inputFile:
    input = pd.read_csv("data/"+file.lower()+'/'+file.lower()+".csv")
    input.to_sql(file, connection, schema='DissertationDatabase', if_exists='append', index=False)
"""
#Read each file about attributes and actions as dataframe and write them to database
for file in inputFile:
    input = pd.read_csv("data/"+file.lower()+'/'+file.lower()+"_action.csv")
    input.to_sql(file.lower()+"_action", connection, schema='DissertationDatabase', if_exists='append', index=False)