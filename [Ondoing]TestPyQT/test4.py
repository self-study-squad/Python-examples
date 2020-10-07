# Test Try method

for i in range(3,-1,-1):
    try:
        value=10/i;
        print("Value=",value)
    except ZeroDivisionError as e:
        print("Error: ",str(e))
        print("ingnore to continue ...")

print("Let's go!!")
