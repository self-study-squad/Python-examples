#  Write a Python program to create set difference. 

setx = set(['apple','mango'])
sety = set(['mango','orange'])
setz = setx & sety
print(setz)
seta = setx - setz
print(seta)