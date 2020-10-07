# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  

x = int(input('Input 1st length: '))
y = int(input('Input 2nd length: '))
z = int(input('Input 3rd length: '))

if x==y==z:
    print('The triangle is Equilateral!')
elif (x==y) or (y==z) or (x==z):
    print('The triangle is Isosceles!')
else:
    print('The triangle is Scalene!')