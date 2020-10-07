# Write a Python program to solve (x + y) * (x + y).

def cal(x,y):
    result = (x + y)**2
    return result

num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number: '))

print('The result must be: %5d'%cal(num_1,num_2))