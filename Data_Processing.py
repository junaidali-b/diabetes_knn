import sqlite3 as sql
import pandas as pd
from Pickle_Backup import backup_env

#Establish SQLite3 connection and create database (Optional step)
db_location = "/home/junaidali_b/Projects/Diabetes_KNN/Data/diabetes.db"
connection = sql.connect(db_location)
cursor = connection.cursor()

#Import data as pandas dataframe
query = "SELECT * FROM raw_data"
raw_data = pd.read_sql_query(query, connection)
#Use pd.read_csv to directly import data from CSV file

#Editing datatypes of columns
int_cols = [0, 1, 2, 3, 4, -2, -1]
for i in int_cols:
    raw_data.iloc[:,i] = raw_data.iloc[:,i].astype(int)
    
float_cols = [5, 6]
for i in float_cols:
    raw_data.iloc[:,i] = raw_data.iloc[:,i].astype(float)

#Updating SQLite3 Database with formatted columns
raw_data.to_sql('raw_data', 
                connection, 
                if_exists = 'replace', 
                index =False)

#Checking for data missing values
raw_data.isnull().sum()

#Performing z-score transformation for all predictors
#This helps in standardising variables when they belong 
#to different units of measurement.

z_data = raw_data
col = list(z_data.iloc[:, :-1].columns)
z_data[col] = (z_data[col] - z_data[col].mean()) / z_data[col].std(ddof = 0)

#Creating table in database for z-score based data
z_data.to_sql('z_data',
              connection,
              if_exists = 'replace',
              index =False)

#Load pickle custom function
exec(open('Pickle_Backup.py').read())

#Backing up variables in the environment
backup_env(db_location,
           # connection, Couldn't back this up
           # cursor, Couldn't back this up
           query,
           raw_data,
           int_cols,
           float_cols,
           z_data,
           col)