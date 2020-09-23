'''
Python program to create a list of tuples from
given list having number and its cube in each tuple
'''
import sys
#Get the Size of Array
try:
    size = int(input("Enter Size of Array:"))
    if size < 0:
        raise Exception
except:
    print("Size must be positive integer")
    sys.exit(0)
    
L = []
while size != 0:
    try:
        num = int(input("Enter a Number:"))
        size = size - 1
        L.append(num)
    except:
        print("Please enter number not other data")

print(L)
#List Comprehension
Output = [(num, num ** 3) for num in L]
print(Output)
