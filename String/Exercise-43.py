#Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder. Go to the editor
#Sample output:
#The area of the rectangle is 1256.66cm2
#The volume of the cylinder is 1254.725cm3
#Click me to see the sample solution

x = 1256.66
y = 1245.725

print('The area of the rectangle is : ' + '{0:.{1}f}cm\u00b2'.format(x,2))
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(y, 3))
