# Write a Python function that accepts a string and calculate the number of upper case 
# letters and lower case letters. 
# Sample String : 'The quick Brow Fox'
# Expected Output : 
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def string_test(s):
    d={"uppercase":0,"lowercase":0}
    for c in s:
        if c.isupper():
            d["uppercase"]+=1
        elif c.islower():
            d["lowercase"]+=1
        else:
            pass
    print("Original String: ",s)
    print('No. of Uppercase characters: ',d["uppercase"])
    print('No. of Lowercase characters: ',d["lowercase"])
    
string_test('The quick Brown Fox')