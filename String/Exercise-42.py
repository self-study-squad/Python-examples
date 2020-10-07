#Write a Python program to count repeated characters in a string. Go to the editor
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2

def diccount(strip):
    dictproc= {}
    for i in strip:
        if i not in dictproc:
            dictproc[i] = 1
        else:
            dictproc[i] += 1
    result = {}
    for i in dictproc: 
        if dictproc[i] != 1:
            result[i] = dictproc[i]
    return result

stringip = input('Input a string: ')
print('String after solving: ')
print(diccount(stringip))