#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def sol(x,y):
    if (x == y) or (x + y == 5) or (abs(x - y) == 5):
        return True
    return False

num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number: '))

print(sol(num_1,num_2))

