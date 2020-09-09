import math
try:
    num = int(input("Enter Number of Natural Numbers:"))
    print(num * (num+1) *(2*num+1) / 6)
except:
    print("Error in Input")
