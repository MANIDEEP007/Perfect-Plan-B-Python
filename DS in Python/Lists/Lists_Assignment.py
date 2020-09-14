L = []
data = open("file.txt").readlines()
for i in data:
    L.append(i.split()[2])
for i in L:
    print(i)
