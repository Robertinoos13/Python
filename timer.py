"""
    Hello and thanks for take a look at this script!
    This script run a timer what supports only seconds and minutes.Working like a normal timer,but with some limits:cant show the hours
    Follow @robert_de_romania on TikTok!
"""

from time import sleep
x = 0 # Seconds
y = 0 # Hours
set = str(input('Enter any key to start the timer'))

while True:
    if x < 10:
        print(f'{y}:0{x}')
        x += 1
        sleep(1)
    else:
        print(f'{y}:{x}')
        x += 1
        sleep(1)
        if x == 60:
            x = 0
            y += 1