L = []

string = ""
while string !="exit":
    string = input("To Skip, Enter Exit. Else, Enter a String:")
    if string !="exit":
        L.append(string)

search = input("Enter Item to be searched")
for each in L:
    if each == search:
        print("Element Exists")
        break
else:
    print("Element Not Exists")
