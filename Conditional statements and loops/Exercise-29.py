# Write a Python program to print alphabet pattern 'X'. Go to the editor
# Expected Output:

# *   *                                                                  
# *   *                                                                  
#  * *                                                                   
#   *                                                                    
#  * *                                                                   
# *   *                                                                  
# *   *

opstr = ''
for row in range(0,7):
    for col in range(0,6):
        if (col == 0 or col == 4) and (row != 2 and row != 3 and row != 4):
            opstr += '*'
        elif (col == 1 or col == 3) and (row == 2 or row == 4):
            opstr += '*'
        elif (col == 2 and row == 3):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)