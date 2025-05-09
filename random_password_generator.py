import random
import string
import time

# Password length question
len = 0
while len <= 4:
    len = int(input("\nWhat length should your password be?: "))
    if len <= 4:
        print("\nPassword needs to be longer than 4 characters.")
        time.sleep(1)
# Password uppercase question
upper = "nan"
while upper != "y" and upper != "n":
    upper = str(input("\nInclue uppercase letters? (y/n): "))
    if upper != "y" and upper != "n":
        print(f"\n{upper} is not a valid answer, only y or n will work.")
        time.sleep(1)
# Password lowercase question
lower = "nan"
while lower != "y" and lower != "n":
    lower = str(input("\nInclue lowercase letters? (y/n): "))
    if lower != "y" and lower != "n":
        print(f"\n{lower} is not a valid answer, only y or n will work.")
        time.sleep(1)
# Password symbols question
symbols = "nan"
while symbols != "y" and symbols != "n":
    symbols = str(input("\nInclue symbols? (y/n): "))
    if symbols != "y" and symbols != "n":
        print(f"\n{symbols} is not a valid answer, only y or n will work.")
        time.sleep(1)

chars = ""
if upper == "y":
    chars += string.ascii_uppercase
if lower == "y":
    chars += string.ascii_lowercase
if symbols == "y":
    chars += string.punctuation

if chars == "":
    print("\nYou didn't pick any character types, can't generate password.")
else:
    password = ""
    for i in range(len):
        password += random.choice(chars)
    print(f"\nGenerated password: {password}")