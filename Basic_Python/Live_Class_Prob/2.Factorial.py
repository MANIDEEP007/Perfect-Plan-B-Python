try:
    n = int(input("Enter a number to compute factorial: "))
    res = 1
    for i in range(n):
        res *= (i+1)
    print(res)
except:
    print("Error in Input")
