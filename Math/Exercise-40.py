# Write a Python program to round a specified decimal by setting 
# precision (between 1 and 4).
# Sample Number : 0.26598
# Original Number : 0.26598
# Precision- 1 : 0.3
# Precision- 2 : 0.27
# Precision- 3 : 0.266
# Precision- 4 : 0.2660
# Expected Output :
# Original Number :  0.26598                                                       
# Precision- 1 : 0.3                                                               
# Precision- 2 : 0.27                                                              
# Precision- 3 : 0.266                                                             
# Precision- 4 : 0.2660

from decimal import *

ipn = Decimal(input('Input a decimal: '))
print('Origin number: {}'.format(ipn))
for i in range(1,5):
    print('Precision - {} : {}'.format(i,round(ipn,i)))