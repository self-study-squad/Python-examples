# Write a Python program to check whether two lists are circularly identical

list_1 = [10,10,0,0,10]
list_2 = [10,10,10,0,0]
list_3 = [1,10,10,0,0]

print('Compare list 1 and list 2: ')
print(' '.join(map(str,list_2)) in ' '.join(map(str,list_1 * 2)))
print('Compare list 1 and list 3: ')
print(' '.join(map(str,list_3)) in ' '.join(map(str,list_1 * 2)))

