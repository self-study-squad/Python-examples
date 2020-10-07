# Write a Python program to display the fraction instances of the
# string representation of a number.
# Sample data : '0.7', '2.5', '9.32', '7e-1'
# Expected Output :
#  0.7 = 7/10                                                                  
#  2.5 = 5/2                                                                  
# 9.32 = 233/25                                                                  
# 7e-1 = 7/10

import fractions

for s in ['0.7','2.5','9.32','7e-1']:
    f = fractions.Fraction(s)
    print('{0:>4} = {1}'.format(s,f))