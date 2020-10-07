# Write a Python function that takes two lists and returns True if they have at least one common member.

def ck(lstip1,lstip2):
    set_1 = set(lstip1)
    set_2 = set(lstip2)
    result = False
    for i in set_1:
        if i in set_2:
            result = True
    return result

print(ck([1,2,3,4,5], [5,6,7,8,9]))
print(ck([1,2,3,4,5], [6,7,8,9]))