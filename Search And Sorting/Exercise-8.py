# Write a Python program to sort a list of elements using the merge sort algorithm.
# Note: According to Wikipedia "Merge sort (also commonly spelled mergesort) is an 
# O(n log n) comparison-based sorting algorithm. Most implementations produce 
# a stable sort, which means that the implementation preserves the input order of
# equal elements in the sorted output."

def mergeSort(nlist):
    print('Spliting ',nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i += 1
            else:
                nlist[k] = righthalf[j]
                j += 1
            k += 1
            
        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j += 1
            k += 1
            
        print('Merging: ',nlist)
        
nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
