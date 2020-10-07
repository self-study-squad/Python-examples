# Write a Python program to print alphabet pattern 'A'.
# Expected Output:

#  ***                                                                   
# *   *                                                                  
# *   *                                                                  
# *****                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *

for i in range(0,7):
    if (i != 0) and (i != 3):
        print(' *   *')
    elif i == 0:
        print('  *** ')
    else:
        print(' *****')
