# Stupid things

def addtofile(fname):
	from itertools import islice
	with open(fname,"w") as adding:
		adding.write('My name is Long! ')
		adding.write('This is a new file with new text in it!')
	txt = open(fname)
	print(txt.read())

addtofile('writetext.txt')
