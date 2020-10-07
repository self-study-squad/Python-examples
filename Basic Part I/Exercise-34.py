#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sumproceed(x,y):
    total = x+y
    if total in range(15,20):
        return 20
    else:
        return total
    
num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number: '))

print('The result will be: %5d'%(sumproceed(num_1,num_2)))