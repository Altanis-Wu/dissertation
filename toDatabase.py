import pandas as pd
import pymysql.cursors

connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', db = 'DissertationDatabase')
cursor = connection.cursor()

def insertRecords(tableName, records):
    insertStr = "INSERT INTO " + tableName + " VALUES (" + records + ");"
    cursor.execute(insertStr)
    result = cursor.fetchall()
    print(result)