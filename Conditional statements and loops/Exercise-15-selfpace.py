# Write a Python program to check the validity of password input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

def check_length(x:str):
    if (len(x)>=6 and len(x)<=16):
        return True
    return False
def check_digit(x:str):
    for p in x:
        if p.isdigit():
            return True
    return False

def check_alpha(x:str):
    for p in x:
        if p.isalpha():
            return True
    return False

def check_specialchar(x:str):
    for p in x:
        if (p == '$' or p == "#" or p == "@"):
            return True
    return False

def check_char(x:str):
    if (check_digit(x) and check_alpha(x) and check_specialchar(x)):
        return True
    return False

input_password = input('Please input a password: ')
if check_length(input_password) and check_char(input_password):
    print('Password is valid!')
else:
    print('Invalid password!')