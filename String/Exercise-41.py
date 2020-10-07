#Write a Python program to strip a set of characters from a string.

vowels = ('a','e','i','o','u')

def dlt(strip,num):
    result = strip[:num]+strip[num+1:]
    return result

def sol(strip):
    result = strip
    for i in vowels: 
        while result.find(i) != -1:
            t = result.find(i)
            print(t)
            result = dlt(result,t)
            print(result)
    return result

stringip = input('Input a string: ')
print('The string after solving is: %s'%sol(stringip))