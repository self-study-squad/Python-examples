# Write a Python program to capitalize first and last letters of each word of a given string. 

str1 = "python exercises practice solution"
str2 = "w3resource"


def ct(str1):
    str1 = result = str1.title()
    print(str1.split())
    result =  ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
        print(result)
    return result[:-1]  

'''
def ct(strip):
    result = ''
    for i in strip:
        if i ==' ':
            result += strip[:i-2] + strip[i-1].upper() + ' ' + strip[i+1].upper() + strip[i+2:]
    result = result.upper(0) + result[1:len(result)]
    return result
'''

print(ct(str1))
print(ct(str2)) 

            