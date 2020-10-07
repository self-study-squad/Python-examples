# Write a Python program to print alphabet pattern 'E'.
# Expected Output:

# *****                                                                  
# *                                                                      
# *                                                                      
# ****                                                                   
# *                                                                      
# *                                                                      
# *****
 
opstr =''
for row in range(0,7):
    for column in range(0,6):
        if column == 0:
            opstr += '*'
        elif (row == 0 or row == 3 or row == 6) and (column == 1 or column == 2 or column == 3):
            opstr += '*'
        elif (row == 0 or row == 6) and column == 5:
            opstr += '*'
    opstr += '\n'
    
print(opstr)