#Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x,y):
    if x > y: 
        z = x
    else:
        z = y
    
    while True:
        if (z % x == 0) and (z % y == 0):
            result = z
            break
        z += 1
    return result

num1 = int(input('Input the first number: '))
num2 = int(input('Input the second number: '))

print(lcm(num1,num2))