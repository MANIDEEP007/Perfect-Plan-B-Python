import sys
a = 0
b = 1
c = 0
try:
    n = int(input("Enter n to find n fibonacci numbers:"))
except:
    print("Error in Input")
    sys.exit(0)
print(a)
print(b)
for _ in range(2,n):
    c = a + b
    a = b
    b = c
    print(c)
