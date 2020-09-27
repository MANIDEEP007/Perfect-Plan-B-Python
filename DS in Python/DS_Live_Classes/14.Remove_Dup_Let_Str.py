string = input("Enter String:")
res = ""

#Without Order
print(''.join(set(string)))

#With Order
for letter in string:
    if letter not in res:
        res += letter
print(res)
