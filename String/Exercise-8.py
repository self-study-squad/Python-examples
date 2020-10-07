#Write a Python function that takes a list of words and returns the length of the longest one.

def sol(list_ip):
    n = 0
    for i in range(len(list_ip)):
        if len(list_ip[i])>len(list_ip[n]):
            n = i
    return n

list_string = input('Please input strings seperate by commas: ')
lst_str = list_string.split(',')
print('Longest length string: %s'%lst_str[sol(lst_str)])