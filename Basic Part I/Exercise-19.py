#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def changestr(s):
    if (len(s)>=2) and (s[:2]=='Is'):
        return s
    else:
        return 'Is'+s

st = input('Input your string: ')
print(changestr(st))