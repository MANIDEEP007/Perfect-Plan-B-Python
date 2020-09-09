try:
    P = float(input("Enter Principal: "))
    R =float(input("Enter Rate of Interest: "))
    T =float(input("Enter Time: "))
    print((P*T*R)/100)
except:
    print("Error in Input")
