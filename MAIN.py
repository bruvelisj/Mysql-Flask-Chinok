import mysql.connector as mysql

db = mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="Mysqljan****",
    database="datubaze"
)
cursor = db.cursor()

# defining the Query
query = "SELECT * FROM artists"

# getting records from the table
cursor.execute(query)

# fetching all records from the 'cursor' object
records = cursor.fetchall()

# Showing the data
for record in records:
    print(record)

# query = "SELECT InvoiceId, Total, "

# query = "SELECT invoices.InvoiceId, invoices.Total, employees.LastName,employees.FirstName, customers.Company From employee JOIN customers ON employees employees.EmployeeId=customers.CustomerId JOIN invoices ON customers customers.CustomerId = invoices.CustomerId;"
# cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)
