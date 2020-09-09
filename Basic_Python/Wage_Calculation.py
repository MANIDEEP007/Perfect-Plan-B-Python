'''
Write a program to prompt the user for days and rate per day to compute total pay.
Use 50 days and a rate of 3.5 per day to test the program.
Total pay is equal to (days* Rate per day).
You should use input to read a string and float() to convert the string to a number.
Don't worry about error checking or bad user data. Good Job!
'''
import sys
try:
    days = int(input("Enter Number of days: "))
except ValueError:
    print("Error in Input!! Days Should be integer")
    sys.exit(0)
try:
    rate_per_day = float(input("Enter Rate Per Day: "))
except ValueError:
    print("Error in Input!! Rate Per day should be a floating number of integer")
    sys.exit(0)
print(days * rate_per_day)
