# Write a Python program to print a complex number and its real 
# and imaginary parts.
# Expected Output :
# Complex Number:  (2+3j)                                                          
# Complex Number - Real part:  2.0                                                 
# Complex Number - Imaginary part:  3.0

import numbers

ipn = complex(2,3)
rlp = ipn.real
imp = ipn.imag
print('Real part: ',rlp)
print('Imagine part: ',imp)