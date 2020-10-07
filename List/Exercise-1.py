# Write a Python program to sum all the items in a list.

def sum_list(listip):
    result = 0 
    for i in listip:
        result += i
    return result

stringip = input('Input a list (seperate by commas): ')
listip = stringip.split(',')
ct = 0
listip = list(map(int, listip))

print('Sum of list: %5d'%sum_list(listip))