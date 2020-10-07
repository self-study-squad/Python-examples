# Write a python program that prints each item and its corresponding type from the following list.
# Sample list: datalist = [1452, 11.23, 1+2j, True ,'w3resource', (0,-1),[5,12], {"class":'V',"section":'A'}]

datalist = [1452, 11.23, 1+2j, True ,'w3resource', (0,-1),[5,12], {"class":'V',"section":'A'}]
for item in datalist:
    print('Type of item ',item,' is ',type(item))