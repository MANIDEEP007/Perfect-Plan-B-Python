try:
    num = int(input("Enter a Number:"))
    res = 0
    for i in str(num):
        res += int(i) ** len(str(num))
    if res == num:
        print("Amstrong Number")
    else:
        print("Not a Amstrong Number")
except:
    print("Error in Input")
