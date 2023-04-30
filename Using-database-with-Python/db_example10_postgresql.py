#!/usr/bin/env python3

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="<fill>", user='<fill>', password='<fill>', host='<fill>', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

cursor = conn.cursor()

cursor.execute("select city_id, city, country_id, last_update from public.city limit 10;")

data = cursor.fetchall()
print(data)

cursor.execute("select city_id, city, country_id, cast(last_update as text) last_update from public.city limit 10;")
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()


#Closing the connection
conn.close()
