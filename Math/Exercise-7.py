# Write a Python program to calculate arc length of an angle. 
# Note: In a planar geometry, an angle is the figure formed by 
# two rays, called the sides of the angle, sharing a common 
# endpoint, called the vertex of the angle. Angles formed by 
# two rays lie in a plane, but this plane does not have to 
# be a Euclidean plane.

# Test Data:
# Diameter of a circle : 8
# Angle measure : 45
# Expected Output :
# Arc Length is : 3.142857142857143

def arclength():
    pi=22/7
    diameter = float(input('Diameter of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    arc_length = (pi*diameter) * (angle/360)
    print("Arc Length is: ", arc_length)

arclength()
