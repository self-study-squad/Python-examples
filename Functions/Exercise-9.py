# Write a Python function that takes a number as a parameter and check the number is 
# prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has 
# no positive divisors other than 1 and itself. 

def checkprime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

p = int(input('Input a number: '))
if checkprime(p):
    print(p,' is a prime number!')
else:
    print(p,' is NOT a prime number!')