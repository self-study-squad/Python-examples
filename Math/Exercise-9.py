# Write a Python program to calculate the discriminant value.
# Note: The discriminant is the name given to the expression 
# that appears under the square root (radical) sign in the quadratic formula. 

# Test Data:
# The x value : 4
# The y value : 0
# The z value : -4
# Expected Output:
# Two Solutions. Discriminant value is : 64.0

def discriminant():
    x_value = float(input('The x value: '))
    y_value = float(input('The y value: '))
    z_value = float(input('The z value: '))
    discriminant = (y_value**2) - (4*x_value*z_value)
    if discriminant > 0:
        print('Two Solution. Discriminant value is: ',discriminant)
    elif discriminant == 0:
        print('One Solution. Discriminant value is: ',discriminant)
    elif discriminant < 0:
        print('No Real Solutions. Discriminant value is: ', discriminant)
        
discriminant()