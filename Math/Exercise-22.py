# Write a python program to find the next smallest palindrome of a 
# specified number. 

def checkpal(x:int):
    if str(x) == str(x)[::-1]:
        return True
    return False

t = int(input('Input a number: '))
n = t + 1
while not checkpal(n):
    n += 1

print(n)

