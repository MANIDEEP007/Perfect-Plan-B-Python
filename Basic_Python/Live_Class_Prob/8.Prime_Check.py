try:
    n = int(input("Enter a Number:"))
except:
    print("Error In Input")
else:
    if n<=1:
        print(n,"Is not a Prime")
    elif n == 2:
        print(n,"Is a Prime")
    else:
        for i in range(2,n//2):
            if n % i == 0:
                print(n,"Is not a Prime")
                break
        else:
            print(n, "Is a Prime")
