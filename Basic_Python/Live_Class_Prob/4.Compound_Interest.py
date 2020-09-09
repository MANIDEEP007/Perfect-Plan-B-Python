try:
    P = float(input("Enter Principal: "))
    R =float(input("Enter Rate of Interest: "))
    T =float(input("Enter Time: "))
    print(P*(1+(R/100))**T)
except:
    print("Error in Input")
