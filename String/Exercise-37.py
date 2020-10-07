#Write a Python program to display a number in left, right and center aligned of width 10

x = 22
print('left: ' + '{:< 20d}'.format(x))
print('right: '+ '{: 20d}'.format(x))
print('center: '+ '{:^ 20d}'.format(x))
print()