#Write a Python program to create a Caesar encryption.

#Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, 
#is one of the simplest and most widely known encryption techniques. 
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
#For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
#The method is named after Julius Caesar, who used it in his private correspondence.


def transcode(strip,numip):
    result = ''
    abc ='abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    no = numip % 26
    for i in strip:
        n = abc.find(i)
        if n != -1:
            n -= no
            if n < 0:
                n += 26
            result += abc[n]
        else:
            n = ABC.find(i)
            n -= no
            if n < 0: 
                n += 26
            result += ABC[n]           
    return result

def createcode(strip,numip):
    result = ''
    abc ='abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    no = numip % 26
    for i in strip:
        n = abc.find(i)
        if n != -1:
            n += no
            if n >= 26: 
                n %= 26
            result += abc[n]
        else:
            n = ABC.find(i)
            n += no
            if n >= 26: 
                n %= 26
            result += ABC[n]        
    return result


loopCon = True
while loopCon:
    choice = input('What process do you want to choose - 1. Translate code - 2. Create code - e - Exit : ')
    if choice == 'e': 
        confirm = input('Do you really want to exit (Y/N)? : ')
        if confirm:
            loopCon = False
            break
    elif choice == str(1):
        stringip = input('Input the code: ')
        num = int(input('Input the step: '))
        result = transcode(stringip,num)
        print('Code Translated: %s'%result)
        result =''
    elif choice == str(2):
        stringip = input('Input the string to create code: ')
        num = int(input('Input the step: '))
        result = createcode(stringip,num)
        print('Code Created: %s'%result)
        result =''
    else:
        choice = input('Your input a mismark. Please input your choice again (1/2/e): ')
        