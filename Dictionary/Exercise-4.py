#  Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(dicip,x):
    if x in dicip:
        print('Key is present in dictionary!')
    else:
        print('Key is not present in dictionary!')

is_key_present(d,0)