# Write a Python program to sum of two given integers. However, 
# if the sum is between 15 to 20 it will return 20.

def alter(x,y:int):
    if 14 < x+y < 21:
        return 20
    else:
        return x+y
    
p = int(input('Input 1st integer: '))
q = int(input('Input 2nd integer: '))
print(alter(p,q))