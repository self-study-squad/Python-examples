#  Write a Python program to split fractional and integer parts of a 
# floating point number. Go to the editor
# Expected Output :
#           (F)  (I)                                                              
# 0/2 = 0.0 (0.0, 0.0)                                                             
# 1/2 = 0.5 (0.5, 0.0)                                                             
# 2/2 = 1.0 (0.0, 1.0)                                                             
# 3/2 = 1.5 (0.5, 1.0)                                                             
# 4/2 = 2.0 (0.0, 2.0)                                                             
# 5/2 = 2.5 (0.5, 2.0)

import math
print('             (F)    (I)')
for i in range(6):
    print('{}/2 = {} {}'.format(i,i/2,math.modf(i/2.0)))