#!/usr/bin/python3

def compute_pay(h, r):
    if h >= 40:
        pay = 40*r
    else:
        pay = h*r

    overtime_pay = 0

    if h >= 40:
        overtime_pay = (h-40)*r*1.5

    total_pay = pay + overtime_pay

    return total_pay

hrs = input("Enter hours worked:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

print("Total pay:", compute_pay(h,r))
