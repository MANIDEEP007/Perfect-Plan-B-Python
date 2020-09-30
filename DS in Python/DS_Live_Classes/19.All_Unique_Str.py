string = input("Enter a String:").lower()
bool_arr = [False] * 128
for letter in string:
    status = bool_arr[ord(letter)]
    if status:
        print(False)
        break
    else:
        bool_arr[ord(letter)] = True
else:
    print(True)
