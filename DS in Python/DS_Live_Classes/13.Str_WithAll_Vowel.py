vowels = "aeiou"
string = input("Enter String:").lower()
vowel_in_str = ""
for letter in string:
    if letter in vowels and letter not in vowel_in_str:
        vowel_in_str += letter
if len(vowels) == len(vowel_in_str):
    print("Accepted")
else:
    print("Not Accepted")
