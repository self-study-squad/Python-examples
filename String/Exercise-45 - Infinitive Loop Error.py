#Write a Python program to check if a string contains all letters of the alphabet.

ck = 'abcdefghijklmnopqrstuvwxyz'


def delt(strip,char):
    result = strip
    t = 0
    while (t != -1) or (len(result) ==0):
        t = result.find(char)
        result = result[:t]+result[t+1:]
    global ck
    t = ck.find(char)
    ck = ck[:t] + ck[t+1:]
    return result

stringip = input('Input a string: ')
while len(stringip) >0:
    charip = stringip[len(stringip)-1]
    stringip = delt(stringip,charip)
if len(ck) == 0:
    print('String contains all the characters!')
else:
    print('String does not contain all the characters!')