import random #Using to Randomly Choose Word
#List of Words
words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "guava",
    "pear",
    "lemon",
    ]

#Number of Turns
turns = 10

#Randomly Pick word from List
guess_word = random.choice(words)

#Valid Choices
correct_choice = "abcdefghijklmnopqrstuvwxyz"

#Guess Made by User
guesses_made = ""

#Progree So far
progress = ""

#Function to check Valid Input
def valid_choice(word):
    if len(word) != 1:
        return False
    if word.lower() not in correct_choice:
        return False
    return True

print("Guess the Fruit")
while turns > 0:
    
    progress = ""
    
    for letter in guess_word:
        if letter in guesses_made:
            progress += letter
        else:
            progress += " _"
    if progress == guess_word:
        print("You Win")
        break
    print(progress)
    
    choice = input("Guess the Letter:")
    valid = False
    while valid != True:
        valid_choice(choice)
        if valid_choice == False:
            print("Pleae enter letter only")
        else:
            guesses_made += choice
            valid = True
    
    else:
        turns = turns -1
        print("You Have %s turns"%(turns))
    
else:
    print("You Lost")
