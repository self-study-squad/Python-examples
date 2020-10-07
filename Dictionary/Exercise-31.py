# Write a Python program to get the key, value and item in a dictionary.

dict_num ={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print('key value count')

for count, (num, val) in enumerate(dict_num.items(),1):
    print('%d    %d    %d'%(num, val, count))