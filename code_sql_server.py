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

df1 = df['emp_salary'].nlargest(1)
print(df1)


df2 = df[df['emp_salary']>50000]
print(df2)

#df2.to_csv("above_salary_employees.csv")

df['emp_id'].duplicated()

