import random

print('Welcome to Guess Number game!')
game_mode = str(input('Please enter game difficulty(EASY-e,NORMAL-n,HARD-h,IMPOSSIBLE-i)'))
game_mode = game_mode.lower()

if game_mode == 'e' or game_mode == 'n' or game_mode == 'h' or game_mode == 'i':
    print('Okay...')
    if game_mode == 'e':
        x = int(input('Enter a number 1-5'))
        number = int(random.uniform(1,6))
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
    elif game_mode == 'n':
        x = int(input('Enter a number 1-10'))
        number = int(random.uniform(1,11))
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
    elif game_mode == 'h':
        x = int(input('Enter a number 1-50'))
        number = int(random.uniform(1,51))
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
    if game_mode == 'i':
        x = int(input('Enter a number 1-100'))
        number = int(random.uniform(1,101))
        print(f'You entered the number {x} and the number what you needed to guess was {number}')
        if x == number:
            print('So,you won!')
        else:
            print('You lose,you can retry restarting the program run')
else:
    print('You gamemode keyword is wrong,please restart the program run')