# Write a Python program to calculate surface volume and area of a cylinder. 
# Note: A cylinder is one of the most basic curvilinear geometric shapes, 
# the surface formed by the points at a fixed distance from a given straight 
# line, the axis of the cylinder.

# Test Data:
# volume : Height (4), Radius(6)
# Expected Output:
# Volume is : 452.57142857142856
# Surface Area is : 377.1428571428571

pi = 22/7

height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi * radian **2)*2)
print('Volume is: ', volume)
print('Surface Area is: ',sur_area)
