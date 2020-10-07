# Write a Python program to print alphabet pattern 'T'. Go to the editor
# Expected Output:
# *****                                                                  
#   *                                                                    
#   *                                                                    
#   *                                                                    
#   *                                                                    
#   *                                                                    
#   *  

opstr = ''
for row in range(0,7):
    for col in range(0,5):
        if col == 2:
            opstr += '*'
        elif row == 0 and col != 2:
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)