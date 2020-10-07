#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def sol(ipstr):
    if (ipstr[-3:] == 'ing') and (len(ipstr)>=3): 
        return ipstr + 'ly'
    elif (len(ipstr)>=3):
        return ipstr + 'ing'
    else:
        return ipstr

str_input = input('Input a string: ')
print('String after solving: %s'%sol(str_input))