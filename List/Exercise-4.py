# Write a Python program to get the smallest number from a list

def smlstnum(lstip):
    result = lstip[0]
    for i in lstip:
        if i<result:
            result = i
    return result


print(smlstnum([1, 2, -8, 0]))