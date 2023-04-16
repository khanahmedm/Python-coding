#!/usr/bin/python3

largest = None
smallest = None

while True:
    sval = input('Enter value:')

    if sval == 'done':
        break

    try:
        fval = int(sval)
    except:
        print('Error: invalid input')
        continue

    if largest is None:
        largest = fval

    if fval > largest:
        largest = fval

    if smallest is None:
        smallest = fval

    if fval < smallest:
        smallest = fval

print('Maximum:', largest)
print('Minimum:', smallest)
