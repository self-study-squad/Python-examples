# Write a Python program to generate random integers in a specific 
# numerical range.
# Expected Output :
# 24 12 72 13 56 80

import random

for x in range(6):
    print(random.randrange(10, 100,2),end=' ')
    
print()
for x in range(10):
    print(random.randint(10,100),end=' ')