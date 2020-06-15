import pandas as pd
from sqlalchemy import create_engine

#Connect to MySQL database
connection = create_engine("mysql+pymysql://root@localhost:3306/DissertationDatabase")