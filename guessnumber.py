"""
    Hello and thanks for take a look at this script!
    This script is a simple game to code using functions from RANDOM,where you need to guess a number between X-Y,with a personalized difficulty
like,EASY,NORMAL,HARD and IMPOSSIBLE.
    Follow @robert_de_romania on TikTok if you want!
"""

import random # Using a library what we need

# Intro and a input to get starded
print('Welcome to Guess Number game!')
game_mode = str(input('Please enter game difficulty(EASY-e,NORMAL-n,HARD-h,IMPOSSIBLE-i)'))
game_mode = game_mode.lower() # Make the string (input) from this:"HeLLo" to this "hello"

if game_mode == 'e' or game_mode == 'n' or game_mode == 'h' or game_mode == 'i': # If u enter a difficulty on a correct way
    print('Okay...')                                                             # The game starting
    if game_mode == 'e': # EASY mode
        x = int(input('Enter a number 1-5')) # Your input,here you guess the correct number
        number = int(random.uniform(1,6)) # Generate a random number between 1.0000...001 and 5.99999...9999
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number: # If your number is equals with the generated number
            print('So,you won!') # You won
        else: # If your input and generated number is different
            print('You lose,you can retry restarting the program run') # You lose
    elif game_mode == 'n': # NORMAL mode
        x = int(input('Enter a number 1-10'))
        number = int(random.uniform(1,11)) # Generate a random number between 1.0000...001 and 10.99999...9999
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
    elif game_mode == 'h': # HARD mode
        x = int(input('Enter a number 1-50'))
        number = int(random.uniform(1,51)) # Generate a random number between 1.0000...001 and 49.99999...9999
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
    if game_mode == 'i': # IMPOSSIBLE mode
        x = int(input('Enter a number 1-100'))
        number = int(random.uniform(1,101)) # Generate a random number between 1.0000...001 and 100.99999...9999
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
else: # If you entered a difficulty in a wrong way
    print('You gamemode keyword is wrong,please restart the program run') # You get an output on console and your run has ended