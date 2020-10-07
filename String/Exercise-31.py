#Write a Python program to print the following floating numbers upto 2 decimal places with a sign

x = 3.1415926
y = -12.9999

print('Original number: %6.2f'%x)
print('Formatted number with signs: '+'{:+.2f}'.format(x))
print('Original number: %6.2f'%y)
print('Formatted number with signs: '+'{:+.2f}'.format(y))