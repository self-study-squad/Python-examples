# Write a Python program to check multiple keys exists in a dictionary.
# Kiểm tra xem các khóa được liệt kê có nằm trong dictionary hay không

stpkeys = {'key1':'value1', 'key2':'value2', 'key3': 'value3'}

print(stpkeys.keys() >= {'key1','key2'})
print(stpkeys.keys() >= {'key1','key2','key4','key5'})
