#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

lst_result = color_list_1 - color_list_2
print(lst_result)