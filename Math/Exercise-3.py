# Write a Python program to calculate the area of a trapezoid.

# Note : A trapezoid is a quadrilateral with two sides parallel. 
# The trapezoid is equivalent to the British definition of the trapezium. 
# An isosceles trapezoid is a trapezoid in which the base angles are equal so.

# Test Data:
# Height : 5
# Base, first value : 5
# Base, second value : 6
# Expected Output: Area is : 27.5

base_1 = 5
base_2 = 6 
height = float(input('Height of trapezoid: '))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = (base_1 + base_2) / 2 * height
print('Area is: ', area)