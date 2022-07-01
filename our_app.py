import database2

#Add a record to the db
# database2.add_one("Laura","Smith","laura@smith.com")

#Delete a record from the db use rowid as string
# database2.del_one('8')

#Add Many Records to DB
# stuff = [
#     ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
#     ('Joshua', 'Raintree', 'joshua@raintree.com')
#     ]
# database2.add_many(stuff)

#Lookup with WHERE
#database2.email_find('john@codemy.com')



#Show All Records
database2.show_all()