#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def checkupper(strip):
    count = 0
    for i in strip[:4]:
        if i.upper() == i:
            count += 1
    if count >= 2: 
        result = strip.upper()
    else:
        result = strip
    return result


stringip = input('Input a string: ')
print('String output: %s'%checkupper(stringip))