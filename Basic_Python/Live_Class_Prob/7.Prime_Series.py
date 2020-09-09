def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2,n//2):
            if n % i == 0:
                return False
        else:
            return True

try:
    a = int(input("Enter Number1:"))
    b = int(input("Enter Number2:"))
except:
    print("Error In Input")
else:
    for i in range(a,b+1):
        if is_prime(i):
            print(i)
