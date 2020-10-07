# Write a Python program to find missing and additional values in two lists. Go to the editor
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h


t1 = 'a b c d e f'
list1 = t1.split(' ')
t2 = 'd e f g h'
list2 = t2.split(' ')

print('Missing value in first list: ',','.join(set(list1).difference(list2)))
print('Missing value in second list: ',','.join(set(list2).difference(list1)))