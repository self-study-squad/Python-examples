# Write a Python program to print alphabet pattern 'P'.
# Expected Output:

# ****                                                                   
# *   *                                                                  
# *   *                                                                  
# ****                                                                   
# *                                                                      
# *                                                                      
# *  

opstr =''
for row in range(0,7):
    for col in range(0,6):
        if (col == 0):
            opstr += '*'
        elif (row == 0 or row == 3) and (0 < col < 4):
            opstr += '*'
        elif (col == 4) and (0 < row < 3):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)