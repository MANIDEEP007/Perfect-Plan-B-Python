try:
    size = int(input("Enter Size of Array:"))
    if size < 0:
        raise Exception
except:
    print("Size must be positive integer")
    sys.exit(0)
    
L = []
while size != 0:
    string = input("Enter a String:")
    size = size - 1
    L.append(string)

word = input("Enter Targer Word:")
occurence = int(input("Enter a number:"))

count =  0
res = []
for each in L:
    if each == word:
        count += 1
        if count == occurence:
           continue
        else:
            res.append(each)
    else:
        res.append(each)
            
print(res)
