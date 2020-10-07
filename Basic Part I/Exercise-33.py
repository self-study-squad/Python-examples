#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def check(x,y,z):
    if (x==y) or (y==z) or (x==z):
        return True
    else:
        return False


num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number: '))
num_3 = int(input('Input the third number: '))

if check(num_1,num_2,num_3):
    print('The result will be: %2d'%(0))
else:
    t = num_1 + num_2 + num_3
    print('The result will be: %4d'%(t))
   