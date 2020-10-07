# Write a Python program to check a dictionary is empty or not.

my_list = {'name': 'longpham', 'CP':'377122966'}
an_empty_list = {}

def ck_empty_list(list):
    if not bool(list):
        return True
    return False

print(ck_empty_list(my_list))
print(ck_empty_list(an_empty_list))
