# Write a Python program to calculate the sum of a list of numbers.

def list_sum(listip):
    if len(listip) == 1:
        return listip[0]
    else:
        return listip[0]+ list_sum(listip[1:])



print(list_sum([2, 4, 5, 6, 7]))