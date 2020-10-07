# Write a Python program to generate random float numbers in a 
# specific numerical range. Go to the editor
# Expected Output :
#  2.036                                                                  
#  36.572                                                                  
#  36.557                                                                  
#  98.051                                                                  
#  37.290                                                                  
#  77.583 

import random
for x in range(6):
    print('{:04.3f}'.format(random.uniform(x, 100)))
    