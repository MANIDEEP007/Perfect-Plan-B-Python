def search(L,x):
    for index in range(0,len(L)):
        if L[index] == x:
            return index
    return -1
L = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
x = input("Enter Search Element:")
print(search(L,int(x)))
