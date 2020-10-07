# Write a Python program to extend a list without append. Go to the editor
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

listip = [10, 20, 30]
listip[:0] = [40,50,60]
print(listip)