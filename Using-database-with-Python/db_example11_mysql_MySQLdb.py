#!/usr/bin/env python3

# Install the following before running the code.
# sudo apt-get install default-libmysqlclient-dev build-essential
# pip install mysqlclient

import MySQLdb

connection = MySQLdb.connect(
        host = "<fill>",
        user = "<fill>",
        password = "<fill>",
        db = "<fill>"
    )

cursor = connection.cursor()
cursor.execute("select @@version")
version = cursor.fetchone()

if version:
    print('Running version: ', version)
else:
    print('Not connected.')

cursor = connection.cursor()
cursor.execute("select * from country limit 10")

row = cursor.fetchone()

while row:
    print(str(row[1]) + '  ' + str(row[3]))
    row = cursor.fetchone()

connection.close()
