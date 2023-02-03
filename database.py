import sqlite3

def create_connection():
    conn = sqlite3.connect('test_db.sqlite')
    return conn

def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)''')
    conn.commit()

def insert_data(conn):
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, salary) VALUES ('John Doe', 50000)")
    c.execute("INSERT INTO employees (name, salary) VALUES ('Jane Doe', 55000)")
    conn.commit()

def retrieve_data(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    return c.fetchall()

def delete_data(conn):
    c = conn.cursor()
    c.execute("DELETE FROM employees")
    conn.commit()

# Create a connection to the SQLite database
conn = create_connection()

# Create the table
create_table(conn)

# Insert some data
insert_data(conn)

# Retrieve and display the data
employees = retrieve_data(conn)
for employee in employees:
    print(employee)

# Delete the data
delete_data(conn)

# Close the connection
conn.close()