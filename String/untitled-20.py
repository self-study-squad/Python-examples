#Write a Python function to reverses a string if it's length is a multiple of 4. 

def callen(strip):
    if len(strip) % 4 == 0:
        return True
    else:
        return False

def reverse(strip):
    result = strip[::-1]
    return result

stringip = input('Input a string: ')
if callen(stringip):
    result = reverse(stringip)
else:
    result = stringip
    
    
    
print('The string after process: %s'%result)