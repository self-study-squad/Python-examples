# Write a Python program to replace dictionary values with their sum.

student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]

def sum_math_v_vi_average(list_of_dict):
    for d in list_of_dict:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dict


print(sum_math_v_vi_average(student_details))
