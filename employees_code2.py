import pandas as pd

df = pd.read_excel('employees_details.xlsx')

print(df.columns)

#df_agg = df.groupby('emp_id')['emp_salary'].sum().reset_index()

#print(df_agg)

dff = df['emp_id'].unique()
print(dff)