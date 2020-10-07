# Write a Python program to print alphabet pattern 'U'. Go to the editor
# Expected Output:

# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
#  *** 

opstr = ''
for row in range(0,8):
    for col in range(0,6):
        if (col == 0 or col == 4) and (row != 7):
            opstr += '*'
        elif (row == 7) and (0 < col < 4):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)