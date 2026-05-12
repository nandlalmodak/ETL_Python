import pandas as pd
from sqlalchemy import create_engine

# Create engine using SQLAlchemy
engine = create_engine(
    "mssql+pyodbc://@LAPTOP-GPVCQ711/master"
    "driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

print("Connection Successful ✅")

# Always use schema name
sqlQuery = "SELECT * FROM dbo.employee_details"

# Read data
df = pd.read_sql(sqlQuery, engine)

print("Full Data:")
print(df)

# Find duplicate emp_id
df_duplicates = df[df['emp_id'].duplicated(keep=False)]

print("Duplicate Records:")
print(df_duplicates)

