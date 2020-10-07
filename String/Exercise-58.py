#Write a Python program to move spaces to the front of a given string.

def rmsp(strip):
    result = strip.replace(' ','')
    return result

def ipsp(strip,num):
    t = num
    strsol = ''
    while num>0:
        num -= 1
        strsol += ' '
    strsol += strip
    return strsol

def ctsp(strip):
    rslt = 0
    for i in strip:
        if i == ' ':
            rslt += 1
    return rslt

stringip = input('Input a string: ')

ct = ctsp(stringip)
strop = rmsp(stringip)
opstr = ipsp(strop,ct)

print('Solution: %s'%opstr)