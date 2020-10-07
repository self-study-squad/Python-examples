# Write a Python program to convert to/from rectangular coordinates
# to Polar coordinates. Go to the editor
# Expected Output :
# Polar Coordinates:  (5.0, 0.9272952180016122)                                    
# Polar to rectangular:  (-2+2.4492935982947064e-16j)

import cmath
cn = complex(3,4)

# get polar coordinates
print('Polar coordinates: ',cmath.polar(cn))

# polar to rectangular. Format for input is (length, <angle in radians>).
cn1 = cmath.rect(2,cmath.pi)
print('Polar to rectangular: ',cn1)