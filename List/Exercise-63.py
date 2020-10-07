# Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

listip = [1,2,3,4]
s = 'emp'

listop = ['emp{0}'.format(i) for i in listip]

print(listop)