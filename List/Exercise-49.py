# Write a Python program to convert list to list of dictionaries. Go to the editor
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

listop = [{'color_name': n,'color_code': c} for n,c in zip(list1,list2)]
print(listop)