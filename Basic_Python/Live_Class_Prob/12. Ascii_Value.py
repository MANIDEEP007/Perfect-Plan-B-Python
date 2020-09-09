import math
try:
    char = input("Enter a Character:")
    if len(char) == 1:
        print(ord(char))
    else:
        print("Character Should be entered Not String")
except:
    print("Error in Input")
