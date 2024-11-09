import time
x = 0
y = 0
set = '?'
set = str(input('start timer by writing S'))
set = set.lower()
if set == 's':
    while True:
        if x < 10:
            print(f'{y}:0{x}')
            x += 1
            time.sleep(1)
        else:
            print(f'{y}:{x}')
            x += 1
            time.sleep(1)
            if x == 60:
                x = 0
                y += 1