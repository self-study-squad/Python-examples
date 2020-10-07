# Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]

dug_list = []
set_list = set()

for x in a:
    if x not in set_list:
        set_list.add(x)
        dug_list.append(x)

print(dug_list)
