#!/usr/bin/env python3

import pyodbc
#import pymssql


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#server = 'tcp:DESKTOP-5F8NRL2'
server = 'tcp:host_ip_address on LAN'
database = 'TEST_DB'
username = ''
password = ''
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
#cnxn = pymssql.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
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
    print (row) 
    row = cursor.fetchone()
