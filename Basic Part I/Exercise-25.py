#Write a Python program to check whether a specified value is contained in a group of values.

def check(num,lst):
    for i in lst:
        if num == i:
            return True
    return False
input_value = int(input('Input a value: '))
check_list = list(input('Input a list with comma seperate: '))

if check(str(input_value),check_list):
    print('Input value is in the check list')
else:
    print('Input value is not in the check list')