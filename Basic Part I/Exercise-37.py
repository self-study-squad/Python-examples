#Write a Python program to display your details like name, age, address in three different lines.

name = input('Input your name: ')
age = int(input('Input your age: '))
address = input('Input your address: ')

print('Name: %s \n Age: %5d \n Address: %s'%(name, age, address))