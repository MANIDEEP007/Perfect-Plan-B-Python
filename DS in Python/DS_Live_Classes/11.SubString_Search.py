import re
string = input("Enter the String:").lower()
search = input("Enter Search String:").lower()

#Method1 - find()
if string.find(search) != -1:
    print("Yes")
else:
    print("No")

#Method2: count
print("Yes" if string.count(search) > 0 else "No")

#Method3: re.search
print("Yes" if re.search(search,string) else "No")


