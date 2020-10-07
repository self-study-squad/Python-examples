__Author__ = 'Danny'


# Program description: This is a calorie counter, specifically for ice cream.
# Input list: people_total: number of people
# cones_total: number of ice cream cones
# Output list: total_calories

# Function Boolean is valid_integer(String input_string)
#   Declare Boolean is_valid
#
#   is_valid = is input string a valid integer?
#   Return is_valid
# End Function

def is_valid_integer(input_string):
    try:
        val = int(input_string)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


# Function Integer get_number_of_ice_cream_cones()
#   Declare String cones_total
#   Declare Boolean is_valid
#
#   Display "How many ice cream cones would you like?"
#   Input cones_total
#   Set is_valid = is_valid_integer(cones_total)
#   While Not is valid
#       Display "Nobody eats half a cone. Please enter a whole number!"
#       Input cones_total
#       is_valid = is_valid_integer(cones_total)
#   End While
#   input_integer = int(cones_total)
#   Return input_integer
# End function
def get_number_of_ice_cream_cones():
    cones_total = input("How many ice cream cones would you like? ")
    is_valid = is_valid_integer(cones_total)
    while not is_valid or not int(cones_total) > 0:
        cones_total = input("Nobody eats half a cone or a negative one. Please enter a whole number!")
        is_valid = is_valid_integer(cones_total)
    input_integer = int(cones_total)
    return input_integer


# Function Integer get_number_of_people()
#   Declare String people_total
#   Declare Boolean is_valid
#
#   Display "How many people are there? "
#   Input people_total
#   Set is_valid = is_valid_integer(people_total)
#   While Not is valid
#       Display "You can't cut people in half and let them eat ice cream! Enter a whole person!"
#       Input people_total
#       is_valid = is_valid_integer(people_total)
#   End While
#   input_integer = int(people_total)
#   Return input_integer
# End function
def get_number_of_people():
    people_total = input("How many people are there? ")
    is_valid = is_valid_integer(people_total)
    while not is_valid or not int(people_total) > 0:
        people_total = input("You can't cut people in half and let them eat ice cream! Enter a whole person!")
        is_valid = is_valid_integer(people_total)
    input_integer = int(people_total)
    return input_integer


# Module calculate_total_calories(a)
# Input people_total
# Set a = get_number_of_ice_cream_cones()
# While 0 < people_total <= 10
#   calories_total = people_total * a * 121
#   people_total += 1
#   print calories_total
#   if calories_total == 10: break
#   else: display "We're out of ice cream"
# Call calculate_total_calories(a)
# End module
def calculate_total_calories():
    people_total = get_number_of_people()
    a = get_number_of_ice_cream_cones()
    while 0 < people_total <= 10:
        calories_total = people_total * a * 121
        people_total += 1
        print("Total calories ", calories_total)
        if calories_total == 10:
            break
    else:
        print("We're out of ice cream")


calculate_total_calories()
