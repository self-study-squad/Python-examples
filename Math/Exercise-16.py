# Write a Python program to print all permutations of a given string (including duplicates).


op = []
result = ''
def permute_string(strip,source:str):
    if len(strip) == len(source):
       op.append(strip)
    else:
        strop = ''
        for i in source:
            if not i in strip:
                permute_string(strip+i,source)

s = str(input('Input a string: '))
permute_string(result,s)
print(op)