# Write a Python program to get the square root and exponential of 
# a given decimal number. Go to the editor
# Decimal number : 1.44
# Expected Output :
# Square root of  1.44  is : 1.2                                                   
# exponential of  1.44  is : 4.220695816996552825673328929

from decimal import *
import math

ipn = Decimal(input('x: '))
print('Square root of {} is: {}'.format(ipn,math.sqrt(ipn)))
print('Exponential of {} is: {}'.format(ipn,math.exp(ipn)))