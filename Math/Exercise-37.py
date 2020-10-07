# Write a Python program to find the sum of the following decimal 
# numbers and display the numbers in sorted order. Go to the editor
# Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25
# Expected Output :
# Sum:  20.33                                                                  
# Sorted order:  [Decimal('0.04'), Decimal('2.00'), Decimal('2.45'), 
# Decimal('2.45'), Decimal('2.69'), Decimal('3.45'), Decimal('7.25')]

from decimal import *

data = list(map(Decimal,'0.04 2.00 2.45 2.45 2.69 3.45 7.25'.split()))

print(sum(data))
print(sorted(data))