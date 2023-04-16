#!/usr/bin/python3

hrs = input("Enter hours worked:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

if h >= 40:
    pay = 40*r
else:
    pay = h*r

overtime_pay = 0

if h >= 40:
    overtime_pay = (h-40)*r*1.5

total_pay = pay + overtime_pay
print("Total pay:", total_pay)
