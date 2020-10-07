# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def chck(strip):
    result = True
    if (strip[0] != strip[len(strip)-1]) or (len(strip)<2) :
        result = False
    return result

def ct(lstip):
    countop = 0
    for i in lstip:
        if chck(i):
            countop += 1
    return countop


listip = ['abc', 'xyz', 'aba', '1221']
print('Expected Result: %d'%ct(listip))