s=" 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"
L = s.split()
S = set(L)
for i in S:
    if L.count(i) == 1:
        print(i)
        break
