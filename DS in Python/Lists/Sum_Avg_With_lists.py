L = []
sum_res = 0
while True:
    try:
        n = input("Enter a Number")
        L.append(int(n))
    except:
        if n == "done":
            break
        else:
            continue
print(sum(L)/len(L))
print(len(L))
