string = input("Enter the String:").lower()
for each in string.split():
    if len(each) % 2==0:
        print(each)
