# Write a Python program to generate random even integers 
# in a specific numerical range.
# Expected Output :
# 44 50 46 62 94 14 


import random

for i in range(6):
    print(random.randrange(100,1000,2),end=' ')