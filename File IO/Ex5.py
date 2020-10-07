# Write a Python program to read a file line by line and store it into a list.

def readlbl(fname):
	with open(fname) as f:
		data = f.readlines()
	print(data)

readlbl('notest.txt')