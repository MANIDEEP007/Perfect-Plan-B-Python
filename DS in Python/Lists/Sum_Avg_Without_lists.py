count = 0
sum_res = 0
while True:
    try:
        n = input("Enter a Number")
        n = int(n)
    except:
        if n == "done":
            break
        else:
            continue
    sum_res += n
    count += 1
print(sum_res/count)
print(count)
