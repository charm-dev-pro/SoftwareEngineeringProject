#class To_Do:  view of database items, sorted by date

import sqlite3

# connection and cursor
connection = sqlite3.connect('test.db') #TODO: use 'Project2.db' in final draft, once  To_Do view works
cursor = connection.cursor()

# reorganize table by date (ASC is most recent, DESC is furthest away)
cursor.execute("SELECT * FROM testing_table ORDER BY DATE ASC") #TODO: use 'Project2' in final draft, once To_Do works

'''
# checking this reogranized table
result = cursor.fetchall()
print(result)
'''

# currently the database can be sorted by date and will print correct result to terminal. 

#TODO: GUI implementation of data
# loop through each table entry
# for each line, list_item = cursor.fetchone() 
# display to GUI


# TODO: added to sources.txt:
# https://www.tutorialspoint.com/python_data_access/python_sqlite_order_by.htm