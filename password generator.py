import random
import string 

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    while True:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        if len(pwd) >= min_length:
            meets_criteria = True
            if numbers and not has_number:
                meets_criteria = False
            if special_characters and not has_special:
                meets_criteria = False
            if meets_criteria:
                break

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
