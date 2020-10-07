# Write a Python program to calculate the area of regular polygon.
# Expected Output :
# Input number of sides: 4                                                
# Input the length of a side: 25                                          
# The area of the polygon is:  625.0000000000001

from math import tan, pi

side_no = int(input("Input number of sides: "))
length = float(input("Input length of sides: "))
area = length**2*side_no/(4*tan(pi/side_no))
print('Area of the regular polygon: %2f'%area)