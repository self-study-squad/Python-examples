#Exercise 6:  Write a Python program to read a file line by line store it into a variable.

def file_read(fname):
	with open(fname,'r') as f:
			data = f.readlines()
			print(data)

file_read('notest.txt')