#Write a Python program to remove the characters which have odd index values of a given string. 

def evensort(strip):
    result = ''
    for i in range(len(strip)):
        if (i % 2 ==0):
            result += strip[i]
    return result

stringip = input('Input a string: ')
print('String output will be: %s'%evensort(stringip))