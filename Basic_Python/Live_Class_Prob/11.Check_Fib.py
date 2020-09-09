import sys
a = 0
b = 1
c = 0
try:
    n = int(input("Enter a number:"))
except:
    print("Error in Input")
    sys.exit(0)
if n == a:
    print(n,"is Fibonacci Number")
    sys.exit(0)
if n == b:
    print(n,"is Fibonacci Number")
    sys.exit(0)
while True:
    c = a + b
    if n == c:
        print(n,"is Fibonacci Number")
        break
    a = b
    b = c
    if c > n:
        print(n,"is not Fibonacci Number")
        break
