# Write a Python program to assess if a file is closed or not.


f = open('text.txt','r')
print(f.closed)
f.close()
print(f.closed)