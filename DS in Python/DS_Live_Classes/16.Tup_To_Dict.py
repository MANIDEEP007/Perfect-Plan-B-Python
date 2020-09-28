list_of_tuples =[("akash", 10), ("gaurav", 12), ("anand", 14),\
("suraj", 20), ("akhil", 25), ("ashish", 30)]

#Method1 - Looping
res_dic = {}
for k,v in list_of_tuples:
    res_dic.setdefault(k,[]).append(v)

print(res_dic)

#Method2 - Builtin
print(dict(list_of_tuples))
