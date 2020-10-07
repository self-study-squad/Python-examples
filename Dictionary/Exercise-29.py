# Write a Python program to remove spaces from dictionary keys.

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print(student_dict)