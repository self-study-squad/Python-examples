# Write a Python program to print the floating point from mantissa, 
# exponent pair. Go to the editor
# Expected Output :
# Mantissa  Exponent  Floating point value                                         
# --------  --------  --------------------                                         
#    0.70       -3     0.09                                                        
#    0.30        0     0.30                                                        
#    0.50        3     4.00 

import math

print('{:^7}  {:^8} {:^17}'.format('Mantissa','Exponent','Floating point value'))
print('{:-^8}  {:-^8}  {:-^20}'.format('','',''))

for m, e in [(0.7, -3),
             (0.3, 0),
             (0.5, 3),
             ]:
    x = math.ldexp(m,e)
    print('{:7.2f}  {:7d}  {:7.2f}'.format(m,e,x))