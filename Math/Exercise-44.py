# Write a Python program to create the fraction instances of 
# float numbers. Go to the editor
# Sample numbers: 0.2, 0.7, 6.5, 6.0
# Expected Output :
# 0.2 = 3602879701896397/18014398509481984                                         
# 0.7 = 3152519739159347/4503599627370496                                          
# 6.5 = 13/2                                                                  
# 6.0 = 6

import fractions
for n in [0.2,0.7,6.5,6.0]:
    print('{} = {}'.format(n, fractions.Fraction(n)))