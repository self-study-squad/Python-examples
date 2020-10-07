# Write a Python program to get the length and the angle of a complex number. Go to the editor
# Expected Output :
# Length of a complex number:  5.0                                                 
# Complex number Angle:  1.5707963267948966

import cmath
cn = complex(3,4)

print('Length of complex num {} is: {}'.format(cn,abs(cn)))
print('Complex num {} have angle: {}'.format(cn,cmath.phase(0+1j)))