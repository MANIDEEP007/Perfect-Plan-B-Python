'''
Swap Elements at given positions
'''
#Swap
#Pop,Insert
#Tuple Pack, Unpack
import sys
#Get the Size of Array
try:
    size = int(input("Enter Size of Array:"))
    if size < 0:
        raise Exception
except:
    print("Size must be positive integer")
    sys.exit(0)
    
L = []
while size != 0:
    try:
        num = int(input("Enter a Number:"))
        size = size - 1
        L.append(num)
    except:
        print("Please enter number not other data")

#Get Positions
pos1 = int(input("Enter Position1:"))
pos2 = int(input("Enter Position1:"))

#Method1 - Swap Logic
try:
    L[pos1-1],L[pos2-1] = L[pos2-1],L[pos1-1] 
except IndexError:
    print("Postion does not exist")

print(L)

#Method2 - Pop & Insert
try:
    first = L.pop(pos1-1)
    second = L.pop(pos2-2)
    L.insert(pos1-1,second)
    L.insert(pos2-1,first)
    
except IndexError:
    print("Position does not exist")
    
print(L)

#Method3 - Tuple Pacck & Unpack
try:
    get = L[pos2-1],L[pos1-1]
    L[pos1-1],L[pos2-1] = get
    
except IndexError:
    print("Position does not exist")

print(L)
