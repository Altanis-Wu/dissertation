import pandas as pd
from sqlalchemy import create_engine
#List of name of tables which
inputFile = ['Age', 'Cars', 'Children', 'Gender', 'Married', 'Social', 'Working']
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")
for file in inputFile:
    input = pd.read_csv("data/"+file.lower()+'/'+file.lower()+".csv")
    input.to_sql(file, connection, schema='DissertationDatabase', if_exists='append', index=False)