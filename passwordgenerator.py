import random

letters = 'qwertyuiopasdfghjklzxcvbnm'
selected_letters = random.choice(letters)
selected_letters1 = random.choice(letters)
selected_letters2 = random.choice(letters)
selected_letters3 = random.choice(letters)
selected_letters4 = random.choice(letters)
numbers = '1234567890'
selected_numbers = random.choice(numbers)
selected_numbers1 = random.choice(numbers)
simbols = '£$&#@'
selected_simbol = random.choice(simbols)
password = str(selected_letters + selected_letters1 + selected_letters2 + selected_letters3 + selected_letters4 + selected_numbers + selected_numbers1 + selected_simbol)
password = password.capitalize()
print(password)