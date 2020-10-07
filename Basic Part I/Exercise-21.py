#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def check(num):
    if num % 2 ==0:
        return True
    else:
        return False

n = int(input('Input a number for checking: '))
if check(n):
    print('%d is an Even number'%(n))
else:
    print('%d is an Odd number'%(n))