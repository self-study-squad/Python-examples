# Write a Python program to sort a list of elements using shell sort algorithm.
# Note : According to Wikipedia "Shell sort or Shell's method, is an in-place 
# comparison sort. It can be seen as either a generalization of sorting by exchange
# (bubble sort) or sorting by insertion (insertion sort). The method starts by sorting
# pairs of elements far apart from each other, then progressively reducing the gap
# between elements to be compared. Starting with far apart elements can move some
# out-of-place elements into position faster than a simple nearest neighbor exchange."

def ShellSort(listip:list):
    n = len(listip)//2
    while n>0:
        for i in range(n,len(listip)):
            for j in range(n,0,-i):
                if listip[j]>listip[i]:
                    temp = listip[i]
                    listip[i] = listip[j]
                    listip[j] = temp
                
        n //= 2


nlist = [14,46,43,27,57,41,45,21,70]
ShellSort(nlist)
print(nlist)