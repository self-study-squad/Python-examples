# Write a Python program to get the local and default precision.
# Expected Output :
# Local precision: 2                                                               
# 22/7 = 3.1        
# Default precision: 28                                                            
# 22 /7 = 3.142857142857142857142857143

import decimal
with decimal.localcontext() as context:
    context.prec = 2
    print('Local precision: ', context.prec)
    print('22/7 = ', (decimal.Decimal('22')/7))
    
print()
print('Default precision: ',decimal.getcontext().prec)
print('22/7 = ',(decimal.Decimal('22')/7))