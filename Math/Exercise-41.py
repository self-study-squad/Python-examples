# Write a Python program to round a specified number upwards 
# towards infinity and down towards negative infinity of precision 4.
# Expected Output :
# 1/17 =  0.05882352941176470588235294118                                          
# Precision:  4                                                                  
# Round upwards towards infinity:  0.05883                                         
# Round down towards negative infinity:  0.05882

import decimal
context = decimal.getcontext()
value = decimal.Decimal(1) / decimal.Decimal(17)
print('1/17 = ',value)
context.prec = 4
print('Precision: ',4)

context.rounding = getattr(decimal, 'ROUND_CEILING')
value = decimal.Decimal(1) / decimal.Decimal(17)
print('Round upwards towards infinity: ',value)

context.rounding = getattr(decimal, 'ROUND_FLOOR')
value = decimal.Decimal(1) / decimal.Decimal(17)
print('Round down towards negative infinity: ',value)