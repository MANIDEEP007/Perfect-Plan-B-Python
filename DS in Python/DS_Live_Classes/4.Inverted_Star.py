'''
Inverted Star Pattern
'''
import sys
try:
    n = int(input("Enter a Number:"))
except:
    print("Sorry, You have not entered number")
    sys.exit(0)

for index in range(0,n):
    print(index*' ' + (n-index)*'*')
