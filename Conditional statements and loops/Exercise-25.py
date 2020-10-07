# Write a Python program to print alphabet pattern 'R'. Go to the editor
# Expected Output:

# ****                                                                   
# *   *                                                                  
# *   *                                                                  
# ****                                                                   
# * *                                                                    
# *  *                                                                   
# *   *

opstr = ''
for row in range(0,7):
    for col in range(0,6):
        if col == 0:
            opstr += '*'
        elif (col == 1) and (row == 0 or row == 3):
            opstr += '*'
        elif (col == 2) and (row == 0 or row == 3 or row == 4):
            opstr += '*'
        elif (col == 3) and (row == 0 or row == 3 or row == 5):
            opstr += '*'
        elif (col == 4) and (row == 1 or row == 2 or row == 6):
            opstr += '*'
        else: 
            opstr += ' '
    opstr += '\n'
print(opstr)