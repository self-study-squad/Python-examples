# Write a Python program to add, subtract, multiply and divide two 
# fractions. Go to the editor
# Expected Output :
# 2/3 + 3/7 = 23/21                                                                
# 2/3 - 3/7 = 5/21                                                                 
# 2/3 * 3/7 = 2/7                                                                  
# 2/3 / 3/7 = 14/9 

import fractions

f1 = fractions.Fraction(2,3)
f2 = fractions.Fraction(3,7)

print('{} + {} = {}'.format(f1,f2,f1 + f2))
print('{} - {} = {}'.format(f1,f2,f1 - f2))
print('{} * {} = {}'.format(f1,f2,f1 * f2))
print('{} / {} = {}'.format(f1,f2,f1 / f2))