#Write a Python program to concatenate all elements in a list into a string and return it.

ip_list = input('Input list ot concate: ')
dc_list = ip_list.split(',')
str_output = ''
for i in range(len(dc_list)):
    str_output += dc_list[i]
print('List after concate: %s'%(str_output))