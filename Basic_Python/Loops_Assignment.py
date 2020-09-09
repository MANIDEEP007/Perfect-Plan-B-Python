'''
Write a program which repeatedly reads numbers until the user enters "exit".
Once "exit" is entered, print out the sum, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try
and except and print an error message and skip to the next number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data Invalid input
Enter a number: exit
9.0 2 4.5
'''
sum_res = 0
count = 0
avg = 0
while True:
    num = input("Enter a Number:")
    if str(num) == "exit":
        break
    try:
        int(num)
        sum_res += int(num)
        count += 1
        
    except:
        print("bad data Invalid input")
if count > 0:
    print(sum_res,count,sum_res/count)
else:
    print("Data Not Sufficient")
