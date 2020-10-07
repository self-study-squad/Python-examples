# Write a Python program to convert a tuple to a dictionary.

tuplex = ((2,'w'),(3,'r'))
dicx = dict((y,x) for x,y in tuplex)
print(dicx)
# print(dict((y,x) for x,y in tuplex))