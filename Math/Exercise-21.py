# Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than 
# or equal to a specified number.
# In mathematics, the sieve of Eratosthenes, one of a number of prime number sieves, 
# is a simple, ancient algorithm for finding all prime numbers up to any given limit.
# It does so by iteratively marking as composite (i.e., not prime) the multiples of
# each prime, starting with the multiples of 2.

k = int(input('Input a number: '))

def listOfN(x:int):
    result = []
    for i in range(x):
        result.append(i)
    return result

def delxy(x,y:list):
    result = list(set(y)-set(x))
    return result

def createTemp(p,q:int):
    result = []
    mul = p
    while mul <= q:
        result.append(mul)
        mul += p
    return result
        
    
n = listOfN(k)
for i in range(2,k):
    listTemp = createTemp(i,k)
    listTemp = listTemp[1:]
    n = delxy(listTemp,n)
    
n = n[2:]
n = sorted(n)
print(n)

