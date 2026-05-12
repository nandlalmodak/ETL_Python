import pyodbc
import pandas as pd
#import os
#from datetime import datetime

#create sql connection
connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host ='LAPTOP-GPVCQ71I',
                                   Datababase ="master",
                                   Trusted_Connection ='yes')
#sql command to read data
sqlQuery ="SELECT * FROM employee_details"
df = pd.read_sql(sqlQuery, connection)
print(df)

df1 = df[df['emp_id'].duplicated()]
print(df1)

