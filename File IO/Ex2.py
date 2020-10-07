
def file_read_lines(fname,numlines):
	from itertools import islice
	with open(fname) as f:
		for line in islice(f,numlines):
			print(line)

file_read_lines('text.txt',2)