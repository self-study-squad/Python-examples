#Write a Python program to find the maximum occurring character in a given string.

str1 = 'Python: Get file creation and modification date/times'
str2 = 'abcdefghijkb'

def chk(strip):
    ch =''
    max = -1
    ascii_no = 256
    dicsave = [0] * ascii_no
    for i in strip:
        dicsave[ord(i)] += 1
    for i in strip:
        if max < dicsave[ord(i)]:
            max = dicsave[ord(i)]
            ch = i
    return ch

print(chk(str1))
print(chk(str2))

        