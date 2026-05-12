import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-GPVCQ71I;'
                      'Database=master;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee_details")
for row in cursor:
    print(row)

