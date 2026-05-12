import pandas as pd
import pytest
#df= pd.read_excel('C:\ETL_Python\employees_details.xlsx')
df= pd.read_excel('employees_details.xlsx')
#df= pd.read_csv('Data.csv')
#print(df)

#df['emp_id'].unique()

df_agg = df.groupby('emp_id')['emp_salary'].sum().reset_index()
print(df_agg)
#print(df.columns)


