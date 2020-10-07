# Write a Python program to get the factorial of a non-negative integer.

def factorial(n):
    if n <= 1: 
        return 1
    else:
        return n * factorial(n-1)

n = int(input('Input a number: '))
print('n! = {}'.format(factorial(n)))