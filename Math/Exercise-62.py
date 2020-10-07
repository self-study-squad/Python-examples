# Write a Python program to calculate a grid of hexagon coordinates
# of the given radius given lower-left and upper-right coordinates. 
# The function will return a list of lists containing 6 tuples of x, y
# point coordinates. These can be used to construct valid regular 
# hexagonal polygons. 

import random

print('************************')
print('** A Simple Math Quiz **')
print('************************')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Integer Division')
print('5. Exit')
print('------------------------')
ct = 0
n = 0
t = 0
while t != 5:
    t = int(input('Enter your choice: '))
    if t == 1:
        n += 1
        a = random.randint(1,100)
        b = random.randint(1,100)
        print('Enter your answer')
        c = int(input('{} + {} = '.format(a,b)))
        if c == a + b:
            print('Correct!')
            ct += 1
        else:
            print('You are wrong!')
        continue
    elif t == 2:
        n += 1
        a = random.randint(1,100)
        b = random.randint(1,100)
        print('Enter your answer')
        c = int(input('{} - {} = '.format(a,b)))
        if c == a - b:
            print('Correct!')
            ct += 1
        else:
            print('You are wrong!')
        continue        
    elif t == 3:
        n += 1
        a = random.randint(1,100)
        b = random.randint(1,100)
        print('Enter your answer')
        c = int(input('{} * {} = '.format(a,b)))
        if c == a * b:
            print('Correct!')
            ct += 1
        else:
            print('You are wrong!')
        continue        
    elif t == 4:
        n += 1
        a = random.randint(1,100)
        b = random.randint(1,100)
        print('Enter your answer')
        c = float(input('{} / {} = '.format(a,b)))
        if c == a / b:
            print('Correct!')
            ct += 1
        else:
            print('You are wrong!')
        continue        
    
print('----------------------------------')
print('You answered {} questions with {} correct'.format(n,ct))
print('Your score is {}%. Thank you.'.format(ct/n*100))