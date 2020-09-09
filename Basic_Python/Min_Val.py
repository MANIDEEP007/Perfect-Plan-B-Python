L = [9,41,12,3,74,15]
res = None
for each in L:
    if res == None:
        res = each
    elif res > each:
        res = each
print(res)
