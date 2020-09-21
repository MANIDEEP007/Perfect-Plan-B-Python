L = [3,4,5,6,10,1] #Random List

#Method1 a,b=b,a
L[0],L[-1] = L[-1],L[0]
print(L)

#Method2 t=a, a=b, b=t Using Temp Var
temp = L[0]
L[0] = L[-1]
L[-1] = temp
print(L)

#Method3 - Tuple Pack and Unpack
get_items = L[-1],L[0]
L[0],L[-1] = get_items
print(L)

#Using Pop & Insert
a = L.pop(0)
b = L.pop(-1)
L.append(a) #Add at the end of List
L.insert(0,b) #Index, Element
print(L)
