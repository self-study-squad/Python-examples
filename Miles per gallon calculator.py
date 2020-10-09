__Author__ = 'Quan Duong'

# !/usr/bin/env python3
import re

# display a welcome message
print("The Miles Per Gallon application")
print()


def is_valid_float(input_value):  # number input validation
    try:
        value = float(input_value)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


def get_miles_driven():
    miles_driven = input("Enter miles driven:         ")
    is_valid = is_valid_float(miles_driven)
    while not is_valid or not float(miles_driven) > 0:
        print("Enter positive numbers only! ")
        is_valid = is_valid_integer(miles_driven)
    miles_gone = float(miles_driven)
    return miles_gone


def get_gallons_used():
    gallons_used = input("Enter gallons of gas used:  ")
    is_valid = is_valid_float(gallons_used)
    while not is_valid or not float(gallons_used) > 0:
        print("Enter positive numbers only!    ")
    gallons_consumed = float(gallons_used)
    return gallons_consumed


def get_gas_price():
    gas_price = input("Enter gas price:    ")
    is_valid = is_valid_float(gas_price)
    while not is_valid or not float(gas_price) > 0:
        print("Enter positive numbers only!    ")
    current_gas_price = float(gas_price)
    return current_gas_price


def calculate():
    gallons_consumed = get_gallons_used()
    current_gas_price = get_gas_price()
    miles_gone = get_miles_driven()
    # calculation
    miles_per_gallon = round(miles_gone / gallons_consumed, 2)
    total_cost = round(gallons_consumed * current_gas_price, 2)
    cost_per_mile = round(total_cost / miles_gone, 2)
    result = (str(miles_per_gallon), str(total_cost), str(cost_per_mile))
    return result


def output():
    result = calculate()
    print()
    print("Miles per gallon: " + result[0])
    print("Total Cost: " + result[1])
    print("Cost per mile: " + result[2])


def repeat_input():
    output()
    another_trip = "y"
    while another_trip == "y":
        another_trip = input("Do you want to continue (y/n)? ")
        if another_trip == "y":
            output()
        elif another_trip != "n":
            print("Please enter only 'y' or 'n' ")
            another_trip = input("Do you want to continue (y/n)? ")
            output()
        else:
            print("Thank you for using mpg calculator")
    print("Bye")


repeat_input()
