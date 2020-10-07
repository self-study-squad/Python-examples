# Write a Python program to generate all sublists of a list.

def sub_lists(listip):
    result =[[]]
    for i in range(len(listip)):
        n = i + 1
        while n <= len(listip):
            st = listip[i:n]
            result.append(st)
            n += 1
    return result

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))