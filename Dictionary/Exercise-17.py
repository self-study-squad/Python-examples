# Write a Python program to remove duplicates from Dictionary.

student_data = { 'id1':{'code': 39, 'name': 'long pham', 'class':'V'},
                 'id2':{'code': 32, 'name': 'nguyen duy', 'class':'V'},
                 'id3':{'code': 32, 'name': 'nguyen duy', 'class':'V'} }

result ={}
for cd, it in student_data.items():
    if it not in result.values():
        result[cd] = it

print(result)