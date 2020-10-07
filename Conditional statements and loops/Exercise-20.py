#  Write a Python program to print alphabet pattern 'G'. Go to the editor
# Expected Output:

# ***                                                                   
#*   *                                                                  
#*                                                                      
#* ***                                                                  
#*   *                                                                  
#*   *                                                                  
# *** 

opstr =''
for row in range(0,7):
    for column in range(0,6):
        if (column == 0) and (row != 0 and row != 6):
            opstr += '*'
        elif (column == 1) and (row == 0 or row == 6):
            opstr += '*'
        elif (column == 2 or column == 3) and (row == 0 or row == 3 or row == 6):
            opstr += '*'
        elif (column == 4) and (row == 1 or row == 3 or row == 4 or row == 5):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'
print(opstr)