L = []

string = ""
while string !="exit":
    string = input("To Skip, Enter Exit. Else, Enter a String:")
    if string !="exit":
        L.append(string)

count = 0

for _ in L:
    count+=1
print(count)
