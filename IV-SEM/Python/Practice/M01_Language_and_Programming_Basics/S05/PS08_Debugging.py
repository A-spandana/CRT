'''try:
    a = int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input")'''

import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input("enter a"))
b = int(input("enter b"))
print(add(a,b))
