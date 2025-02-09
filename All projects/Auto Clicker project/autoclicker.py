"""
    Hello,thanks for take a look at this script!
    This script its one of most simplest AUTOCLICKER script,what include the display cordonates with X/Y axis to make clicks with PYAUTOGUY,a
loop for repeated clicks and using a pause script function from TIME library
    Follow @robert_de_romania on TikTok if you want!
"""


import pyautogui # The library what help us to make the clicks on a automatic mode
from time import sleep # We use only a function from TIME library

# The cordonates where we want to make the clicks
x_loc = 490
y_loc = 600

# Total number clicks
num_clicks = 99999

# A click every ... seconds
interval = 2

# Time to be ready
sleep(5)

for _ in range(num_clicks):
    # Autoclicks loop
    pyautogui.click(x=x_loc, y=y_loc)
    sleep(interval)