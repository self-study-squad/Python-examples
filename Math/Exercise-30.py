#  Write a Python program to find the roots of a quadratic function. 
# Expected Output :
# Quadratic function : (a * x^2) + b*x + c                                
# a: 25                                                                   
# b: 64                                                                   
# c: 36                                                                   
# There are 2 roots: -0.834579 and -1.725421

import math

a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

delta = b**2 - 4*a*c
sqrtdelta = math.sqrt(delta)

x1 = (-b + sqrtdelta)/(2*a)
x2 = (-b - sqrtdelta)/(2*a)

print('There are roots: %2f ; %2f'%(x1,x2))