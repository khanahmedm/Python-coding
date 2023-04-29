#!/usr/bin/env python3

import pymssql

# fill the parameter values for the connection string
cnxn = pymssql.connect(server='<fill>', user='<fill>', password='<fill>', database='<fill>')

cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

cursor.execute("SELECT * FROM EMPLOYEES") 
row = cursor.fetchone() 
while row:
    print (str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2])) 
    row = cursor.fetchone()
