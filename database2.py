import sqlite3

#this would connect a db in memory
#conn = sqlite3.connect(':memory:')

#Query the DB and Return All Records
def show_all():
    #Connect to database
    conn = sqlite3.connect('customers.db')
    #create a cursor
    c = conn.cursor()
    
    #Query the database and Display
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()

#Add a New Record to the Table
def add_one(first,last,email):
    conn = sqlite3.connect('customers.db')
    c=conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()

#Delete a Record from the Table
def del_one(id):
    conn = sqlite3.connect('customers.db')
    c=conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()

#Add Many Records to the Table
def add_many(list):
    conn = sqlite3.connect('customers.db')
    c=conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()

#Lookup with WHERE
def email_find(email):
    conn = sqlite3.connect('customers.db')
    c=conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)
    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()