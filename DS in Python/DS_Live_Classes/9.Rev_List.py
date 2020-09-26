L = []

string = ""
while string !="exit":
    string = input("To Skip, Enter Exit. Else, Enter a String:")
    if string !="exit":
        L.append(string)

#Method1:Slicing
L = L[::-1]
print(L)

#Method2 - reversed()
L = list(reversed(L))
print(L)

#Method3 - reverse()
L.reverse()
print(L)
