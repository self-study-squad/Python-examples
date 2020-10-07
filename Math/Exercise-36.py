# Write a Python program to find the maximum and minimum numbers 
# from the specified decimal numbers. Go to the editor
# Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25
# Expected Output :
# Maximum:  7.25                                                                  
# Minimum:  0.04

from decimal import *

data = list(map(Decimal,'2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print('Max: ',max(data))
print('Min: ',min(data))
print(data)