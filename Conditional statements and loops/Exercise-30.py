# Write a Python program to print alphabet pattern 'Z'. Go to the editor
# Expected Output:

# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******

opstr = ''
for row in range(0,8):
    for col in range(0,8):
        if (row == 0 or row == 7):
            opstr += '*'
        elif col == 7 - row:
            opstr += '*'
        else:
            opstr +=' '
    opstr += '\n'
print(opstr)