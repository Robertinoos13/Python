sign = str(input('Write one of this signs +,-,:,x,avr,%2 or %:'))
numbers = int(input('How much numbers do you want to calculate?'))

#Simplu,doar calculează suma dintre câteva numere,maxim 6
if sign == '+':
    if numbers <= 1 or numbers > 6:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 2:
        x = int(input('?+?'))
        y = int(input(f'{x}+'))
        result = x + y
        print(f'{x}+{y}={result}')
    elif numbers == 3:
        x = int(input('?+?+?'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        result = x + y + z
        print(f'{x}+{y}+{z}={result}')
    elif numbers == 4:
        x = int(input('?+?+?+?'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        a = int(input(f'{x}+{y}+{z}+'))
        result = x + y + z + a
        print(f'{x}+{y}+{z}+{a}={result}')
    elif numbers == 5:
        x = int(input('?+?+?+?+?'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        a = int(input(f'{x}+{y}+{z}+'))
        b = int(input(f'{x}+{y}+{z}+{a}+'))
        result = x + y + z + a + b
        print(f'{x}+{y}+{z}+{a}+{b}={result}')
    elif numbers == 6:
        x = int(input('?+?+?+?+?+?'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        a = int(input(f'{x}+{y}+{z}+'))
        b = int(input(f'{x}+{y}+{z}+{a}+'))
        c = int(input(f'{x}+{y}+{z}+{a}+{b}+'))
        result = x + y + z + a + b + c
        print(f'{x}+{y}+{z}+{a}+{b}+{c}={result}')

#Simplu,doar calculează scăderea dintre câteva numere,maxim 6
elif sign == '-':
    if numbers <= 1 or numbers > 6:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 2:
        x = int(input('?-?'))
        y = int(input(f'{x}-'))
        result = x - y
        print(f'{x}-{y}={result}')
    elif numbers == 3:
        x = int(input('?-?-?'))
        y = int(input(f'{x}-'))
        z = int(input(f'{x}-{y}-'))
        result = x - y - z
        print(f'{x}-{y}-{z}={result}')
    elif numbers == 4:
        x = int(input('?-?-?-?'))
        y = int(input(f'{x}-'))
        z = int(input(f'{x}-{y}-'))
        a = int(input(f'{x}-{y}-{z}-'))
        result = x - y - z - a
        print(f'{x}-{y}-{z}-{a}={result}')
    elif numbers == 5:
        x = int(input('?-?-?-?-?'))
        y = int(input(f'{x}-'))
        z = int(input(f'{x}-{y}-'))
        a = int(input(f'{x}-{y}-{z}-'))
        b = int(input(f'{x}-{y}-{z}-{a}-'))
        result = x - y - z - a - b
        print(f'{x}-{y}-{z}-{a}-{b}={result}')
    elif numbers == 6:
        x = int(input('?-?-?-?-?-?'))
        y = int(input(f'{x}-'))
        z = int(input(f'{x}-{y}-'))
        a = int(input(f'{x}-{y}-{z}-'))
        b = int(input(f'{x}-{y}-{z}-{a}-'))
        c = int(input(f'{x}-{y}-{z}-{a}-{b}-'))
        result = x - y - z - a - b - c
        print(f'{x}-{y}-{z}-{a}-{b}-{c}={result}')

#Împărțirea,folositor pentru a calcula de câte ori intră un număr în altul,maxim 6 numere
elif sign == ':' or sign == '/':
    if numbers <= 1 or numbers > 6:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 2:
        x = int(input('?:?'))
        y = int(input(f'{x}:'))
        result = x / y
        print(f'{x}:{y}={result}')
    elif numbers == 3:
        x = int(input('?:?:?'))
        y = int(input(f'{x}:'))
        z = int(input(f'{x}:{y}:'))
        result = x / y / z
        print(f'{x}:{y}:{z}={result}')
    elif numbers == 4:
        x = int(input('?:?:?:?'))
        y = int(input(f'{x}:'))
        z = int(input(f'{x}:{y}:'))
        a = int(input(f'{x}:{y}:{z}:'))
        result = x / y / z / a
        print(f'{x}:{y}:{z}:{a}={result}')
    elif numbers == 5:
        x = int(input('?:?:?:?:?'))
        y = int(input(f'{x}:'))
        z = int(input(f'{x}:{y}:'))
        a = int(input(f'{x}:{y}:{z}:'))
        b = int(input(f'{x}:{y}:{z}:{a}:'))
        result = x / y / z / a / b
        print(f'{x}:{y}:{z}:{a}:{b}={result}')
    elif numbers == 6:
        x = int(input('?:?:?:?:?:?'))
        y = int(input(f'{x}:'))
        z = int(input(f'{x}:{y}:'))
        a = int(input(f'{x}:{y}:{z}:'))
        b = int(input(f'{x}:{y}:{z}:{a}:'))
        c = int(input(f'{x}:{y}:{z}:{a}:{b}:'))
        result = x / y / z / a / b / c
        print(f'{x}:{y}:{z}:{a}:{b}:{c}={result}')

#Îmulțirea,îmulțește câteva numere pentru a obține un număr mai mare,maxim 6 numere.EXEMPLU : 3*4= 3+3+3+3= 9
elif sign == 'x' or sign == "*":
    if numbers <= 1 or numbers > 6:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 2:
        x = int(input('?x?'))
        y = int(input(f'{x}x'))
        result = x * y
        print(f'{x}*{y}={result}')
    elif numbers == 3:
        x = int(input('?x?x?'))
        y = int(input(f'{x}x'))
        z = int(input(f'{x}x{y}x'))
        result = x * y * z
        print(f'{x}x{y}x{z}={result}')
    elif numbers == 4:
        x = int(input('?x?x?x?'))
        y = int(input(f'{x}x'))
        z = int(input(f'{x}x{y}x'))
        a = int(input(f'{x}x{y}x{z}x'))
        result = x * y * z * a
        print(f'{x}x{y}x{z}x{a}={result}')
    elif numbers == 5:
        x = int(input('?x?x?x?x?'))
        y = int(input(f'{x}x'))
        z = int(input(f'{x}x{y}x'))
        a = int(input(f'{x}x{y}x{z}x'))
        b = int(input(f'{x}x{y}x{z}x{a}x'))
        result = x * y * z * a * b
        print(f'{x}x{y}x{z}x{a}x{b}={result}')
    elif numbers == 6:
        x = int(input('?x?x?x?x?x?'))
        y = int(input(f'{x}x'))
        z = int(input(f'{x}x{y}x'))
        a = int(input(f'{x}x{y}x{z}x'))
        b = int(input(f'{x}x{y}x{z}x{a}x'))
        c = int(input(f'{x}x{y}x{z}x{a}x{b}x'))
        result = x * y * z * a * b * c
        print(f'{x}x{y}x{z}x{a}x{b}x{c}={result}')

#Media(average),folositor pentru a calcula media generală,media mililitrilor din sticle de apă,ect.EXEMPLU:(6+8)/2 = 7 (media generală)
if sign == 'avr':
    if numbers <= 1 or numbers > 6:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 2:
        x = int(input('(?+?)/2'))
        y = int(input(f'({x}+'))
        result = (x + y) / 2
        print(f'({x}+{y})/2={result}')
    elif numbers == 3:
        x = int(input('(?+?+?)/3'))
        y = int(input(f'({x}+'))
        z = int(input(f'({x}+{y}+'))
        result = (x + y + z) / 3
        print(f'({x}+{y}+{z})/3={result}')
    elif numbers == 4:
        x = int(input('(?+?+?+?)/4'))
        y = int(input(f'({x}+'))
        z = int(input(f'({x}+{y}+'))
        a = int(input(f'({x}+{y}+{z}+'))
        result = (x + y + z + a) / 4
        print(f'({x}+{y}+{z}+{a})/4={result}')
    elif numbers == 5:
        x = int(input('(?+?+?+?+?)/5'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        a = int(input(f'{x}+{y}+{z}+'))
        b = int(input(f'{x}+{y}+{z}+{a}+'))
        result = (x + y + z + a + b) / 5
        print(f'({x}+{y}+{z}+{a}+{b})/5={result}')
    elif numbers == 6:
        x = int(input('(?+?+?+?+?+?)/6'))
        y = int(input(f'{x}+'))
        z = int(input(f'{x}+{y}+'))
        a = int(input(f'{x}+{y}+{z}+'))
        b = int(input(f'{x}+{y}+{z}+{a}+'))
        c = int(input(f'{x}+{y}+{z}+{a}+{b}+'))
        result = (x + y + z + a + b + c) / 6
        print(f'({x}+{y}+{z}+{a}+{b}+{c})/6={result}')

#Folositor pentru a afla dintr-un număr cât înseamnă X% procente. EXEMPLU:30% din 100 este 70
elif sign == '%':
    if numbers < 1 or numbers > 1:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 1:
        x = int(input('?% of ?:'))
        y = int(input(f'{x}% of ?:'))
        z = x * 0.01
        result = y * z
        print(f'{x}% of {y} is {result}')

#Folositor pentru a afla câte ?% procente înseamnă un număr dintr-alt număr. EXEMPLU: 20 din 100 este %20
elif sign == '%2':
    if numbers < 1 or numbers > 1:
        print(f'ERROR:You cant calculate {numbers} numbers.Restart program and put a valid value')
    elif numbers == 1:
        y = int(input('? of ? is ?% procents:'))
        a = int(input(f'{y} of ? is ?% procents:'))
        z = y / a
        result = z * 100
        print(f'{y} of {a} is {result}% procents:')
else:
    print('ERROR:Invalid sign.Restart the program and put a valit sign (+,-,x,:,/,avr,%2 or %)')