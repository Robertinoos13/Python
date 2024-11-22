"""
    Hello and thanks for take a look at this script!
    This script generate a password for you,maked with 5 letters,2 numbers and a special character,using the CHOICE function from RANDOM library,
where the CHOICE function select a index from letters,numbers and simbols variabiles,search the character and save the value on a variabile.
    Follow @robert_de_romania if u want!
"""

import random # using RANDOM library

letters = 'qwertyuiopasdfghjklzxcvbnm' # All letters from a keyboard

# All this variabiles save a letter to create your random password
selected_letters = random.choice(letters)
selected_letters1 = random.choice(letters)
selected_letters2 = random.choice(letters)
selected_letters3 = random.choice(letters)
selected_letters4 = random.choice(letters)

numbers = '1234567890' # All numbers from a keyboard

# All this variabiles save a number to create your random password
selected_numbers = random.choice(numbers)
selected_numbers1 = random.choice(numbers)

simbols = '£$&#@' # Some special caracters from keyboard
selected_simbol = random.choice(simbols) # This variabile save a special character to create your random password
password = str(selected_letters + selected_letters1 + selected_letters2 + selected_letters3 + selected_letters4 + selected_numbers + selected_numbers1 + selected_simbol) # Creating your password by adding all values choosed random and save it on a variabile
password = password.capitalize() # Your password is modified form this "fgndl56#" to this "Fgndl56#"
print(password) # And show your password