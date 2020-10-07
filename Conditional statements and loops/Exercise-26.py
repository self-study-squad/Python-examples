# Write a Python program to print the following patterns. Go to the editor
# Expected Output:

#  ****                                                                  
# *                                                                      
# *                                                                      
#  ***                                                                   
#     *                                                                  
#     *                                                                  
# **** 

opstr = ''
for row in range(0,7):
    for col in range(0,6):
        if (col == 0) and (row == 1 or row == 2 or row == 6):
            opstr += '*'
        elif (0 < col < 4) and (row == 0 or row == 3 or row == 6):
            opstr += '*'
        elif (col == 4) and (row == 0 or row == 4 or row == 5):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)