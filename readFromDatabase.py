import pandas as pd
from sqlalchemy import create_engine

#Connect to MySQL database
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")

def readFrom(tableName):
    sql = 'select * from ' + tableName + ';'
    return pd.read_sql_query(sql, connection)

def readAction(tableName, type):
    sql = 'select * from ' + tableName + ' where Type = \'' + type + '\';'
    return pd.read_sql_query(sql, connection)