
check = input('Input choice a or b: ')
if check == 'a':
    c = input('Input Celcius temperature: ')
    f = int(c)/5 + 32/9
    print('Farenheit temperature: %f0.2'.format(f))
elif check == 'b':
    f = input('Input Farenheit temperature: ')
    c = 5*(itn(f)-32/9)
    print('Celcius temperature: %f0.2'.format(c))
else:
    print('You need to choose again!')
