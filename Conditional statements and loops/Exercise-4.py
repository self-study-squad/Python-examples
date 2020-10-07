# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(1,6):
    for j in range(i):
        print('* ',end='')
    print()

for i in range(2,6):
    for j in range(6-i):
        print('* ',end='')
    print()
    