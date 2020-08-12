import pandas as pd
from sqlalchemy import create_engine

#Connect to MySQL database
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")
#The function to read data about different type of people.
def readFrom(tableName, type):
    sql = 'select * from ' + tableName + ' where Type=\"'+type+'\";'
    return pd.read_sql_query(sql, connection)
#The function to read different actions and type of visitors.
def readAction(tableName, type, visitor):
    sql = 'select * from ' + tableName + ' where Type= \'' + type + '\' and Visitor= \'' + visitor +'\';'
    return pd.read_sql_query(sql, connection)
#The function to read certain type of people
def readCertainVisitor(tableName, type, attribute):
    sql = 'select * from ' + tableName + ' where Type=\"' + type + '\" and Attribute= \'' + attribute + '\';'
    return pd.read_sql_query(sql, connection)

def meanAbsoluteError(predict, actual):
    sum = 0;
    for i in range(len(predict)):
        if predict[i]>actual[i]:
            sum+=predict[i]-actual[i]
        else:
            sum+=actual[i]-predict[i]
    return sum/len(predict)