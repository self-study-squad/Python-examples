# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def rev(x:str):
    result = ''
    for i in x:
        result = i + result
    return result

input_string = input('Input a string: ')
print(rev(input_string))