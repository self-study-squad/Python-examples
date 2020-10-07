# Write a Python program to print alphabet pattern 'M'.
# Expected Output:

# *       *                                                             
# *       *                                                             
# * *   * *                                                             
# *   *   *                                                             
# *       *                                                             
# *       *                                                             
# *       *

opstr = ''
for row in range(0,7):
    for col in range(0,7):
        if col == 0 or col == 6:
            opstr += '*'
        elif ((row == 2) and (col == 2 or col == 4)) or ((row == 3) and (col == 3)):
            opstr += '*'
        else:
            opstr += ' '
    opstr += '\n'

print(opstr)