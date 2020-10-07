# Write a Python program to create the fraction instances of decimal
# numbers. Go to the editor
# Sample decimal.2' number: Decimal('0), Decimal('0.7'), 
# Decimal('2.5'), Decimal('3.0')

# Expected Output :
# 0.2 = 1/5                                                                  
# 0.7 = 7/10                                                                  
# 2.5 = 5/2                                                                  
# 3.0 = 3

import decimal
import fractions

values = [
    decimal.Decimal('0.2'),
    decimal.Decimal('0.7'),
    decimal.Decimal('2.5'),
    decimal.Decimal('3.0'),
]

for d in values:
    print('{} = {}'.format(d,fractions.Fraction(d)))
    
t = 0.2
print(fractions.Fraction(t))