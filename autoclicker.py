import pyautogui
import time

#Cordonate unde vrem să facem click-urile
x_loc = 300
y_loc = 400

#Număr clickuri
num_clicks = 99999

#Interval clickuri
interval = 2
#Timp pregătire
time.sleep(5)

for _ in range(num_clicks):
    pyautogui.click(x=x_loc, y=y_loc)
    time.sleep(interval)
