# Exercise 7: Write a Python program to read a file line by line store it into an array.

def file_read(fname):
	content_array = []
	with open(fname,'r') as f:
		for line in f:
			content_array.append(line)
		print(content_array)

file_read('notest.txt')
