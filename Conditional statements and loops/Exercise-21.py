# Write a Python program to print alphabet pattern 'L'.
# Expected Output:

# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****

opstr = ''
for row in range(0,7):
    for col in range(0,6):
        if col == 0:
            opstr += '*'
        elif (row == 6) and (col != 0):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'
print(opstr)