import sys
a = 0
b = 1
c = 0
try:
    n = int(input("Enter n to find nth fibonacci number:"))
except:
    print("Error in Input")
    sys.exit(0)
if n <= 0:
    print("Error in Input")
    sys.exit(0)
if n == 1:
    print(a)
    sys.exit(0)
if n == 2:
    print(b)
    sys.exit(0)
for _ in range(2,n):
    c = a + b
    a = b
    b = c
print(c)
