# Write a Python program to write a list to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("newfile.txt",'w') as f1:
    for c in color:
        f1.write("%s\n"%c)

with open("newfile.txt",'r') as f2:
    print(f2.read())