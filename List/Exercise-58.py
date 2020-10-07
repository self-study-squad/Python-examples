# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

listmain = [1, 3, 5, 7, 9, 10]
listadd = [2, 4, 6, 8]

listmain[-1:] = listadd
print(listmain)
