# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

def solstr(str1,str2):
    t1 = str1[0]
    t2 = str2[0]
    sol1 = str1[1:]
    sol2 = str2[1:]
    str1 = t2 + sol1
    str2 = t1 + sol2
    result = str1 + ' ' + str2
    return result

string1 = input('Please input string no.1: ')
string2 = input('Please input string no.2: ')
print('String after solving: %s'%solstr(string1,string2))