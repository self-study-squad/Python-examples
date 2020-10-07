# Write a Python program which iterates the integers from 1 to 50. For multiples of three print 'Fizz' instead of the number and for the multiples of 
# five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.

def ck5(x:int):
    if x % 5 == 0:
        return True
    else:
        return False

def ck3(x:int):
    if x % 3 == 0:
        return True
    else:
        return False

for i in range(50):
    if (ck3(i) and ck5(i)):
        print('FizzBuzz')
    elif ck3(i):
        print('Fizz')
    elif ck5(i):
        print('Buzz')
    else:
        print(i)
