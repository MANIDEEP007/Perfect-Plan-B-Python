#Method1 - Using Slicing
def palin(string):
    return string.lower() == string.lower()[::-1]

#Method2 - For Loop
def palin1(string):
    string = string.lower()
    for index in range(0,len(string)//2):
        if string[index] != string[len(string)-index-1]:
            return False
    return True

#Method3 - Using Reversed
def palin2(string):
    string = string.lower()
    #Reversed returns a list of characters in string in reverse order
    rev_string = ''.join(reversed(string))
    return string == rev_string

#Get User Input
string = input("Enter a String:")

#Check Palindrome Using Method1
if palin(string):
    print("Yes")
else:
    print("No")

#Check Palindrome Using Method2
if palin1(string):
    print("Yes")
else:
    print("No")

#Check Palindrome Using Method3
if palin2(string):
    print("Yes")
else:
    print("No")
