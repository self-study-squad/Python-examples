# Write a Python program to print alphabet pattern 'O'. Go to the editor
# Expected Output:

#  ***                                                                   
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
#  *** 

opstr = ''

for row in range(0,6):
    for col in range(0,5):
        if ((col == 0) or (col == 4)) and ((row != 0) and (row != 5)):
            opstr += '*'
        elif ((row == 0) or (row == 5)) and ((col != 0) and (col != 4)):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)