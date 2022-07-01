import sqlite3

#this would connect a db in memory
#conn = sqlite3.connect(':memory:')

#Connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

# Create a table (using docstrings)
# c.execute("""CREATE TABLE customers(
#         first_name text,
#         last_name text,
#         email text
#     )""")


#Datatypes
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#sql commands are always capitals
#Insert One Value at a Time
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

#insert Many vales at a time
# many_customers = [
#                     ('Wes', 'Brown', 'wes@brown.com'),
#                     ('Steph', 'Kuewa', 'steph@kuewa.com'),
#                     ('Dan', 'Pas', 'dan@pas.com'),
#                 ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# print("Command executed successfully")

#Update Records
# c.execute("UPDATE customers SET email = 'john@codemy.com' WHERE rowid=1 ")
# c.execute("DELETE from customers WHERE rowid = 6")
# conn.commit()  

#Order By
#Ascending = ASC , Descending = DESC
#c.execute("SELECT rowid, *FROM customers ORDER BY last_name ")
 
#AND/OR
# c.execute("SELECT rowid, *FROM customers WHERE last_name LIKE 'Br%' OR rowid=3 ")

#Limiting
#c.execute("SELECT rowid, *FROM customers ORDER BY rowid DESC LIMIT 2  ")

#Deleting a table called DROP Table
c.execute("DROP TABLE customers ")
conn.commit()
#Query the database

#get rowid out
# c.execute("SELECT rowid, * FROM customers")
#Use where with categories >,<,= or LIKE for specific requests. Can use % as wildcard
#c.execute("SELECT rowid, * FROM customers")
#print(c.fetchall())
#print(c.fetchone()[0])
items = c.fetchall()
# print("NAME" + "\t\t" +" EMAIL")
for item in items:
    # print(item[0], "", item[1], "\t", item[2])
    print(item)
#Commit our command
conn.commit()

#Close our connection
conn.close()
