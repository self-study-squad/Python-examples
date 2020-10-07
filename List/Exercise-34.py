# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. Go to the editor
# Note: In mathematics, the sieve of Eratosthenes
# one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.

def prime_eratosthenes(n):
    result =[]
    for i in range(2,n):
        ck = True
        for j in range(2,i-1):
            if i % j == 0:
                ck = False
        if ck:
            result.append(i)
    return result


print(prime_eratosthenes(100))