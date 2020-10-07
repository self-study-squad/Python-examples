# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

4row_num = int(input('Input number of row: '))
col_num = int(input('Input number of col: '))

multilist = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multilist[row][col] = row*col

for lst in multilist:
    print(lst)