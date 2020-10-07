_author_ = "Quan Duong"
# copyright 2020
# date 10/1/20

"""""
LAB #1
This program will accept 2 numbers from a user and calculate the sum.  
Input List: opInput, num1, num2
Output list: total 
"""""
import math
from datetime import datetime


def is_valid_integer(input_string):  # Input validation function
    try:
        val = float(input_string)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


def signInput():
    todaysDate = datetime.now()
    inputError = True
    while inputError:
        opInput = input("What operator would you like to use as of {} ? (+,-,*,^): ".format(todaysDate))
        if opInput == "+":
            inputError = False
        elif opInput == "-":
            inputError = False
        elif opInput == "*":
            inputError = False
        elif opInput == "/":
            inputError = False
        else:
            print("Please print with the given operator!")
            inputError = True
    return opInput


def inputNum1():
    num1 = input("Type your first number: ")
    is_valid = is_valid_integer(num1)
    while not is_valid or not float(num1):
        print("Please enter a valid number!")
        num1 = input("Type your first number: ")
        is_valid = is_valid_integer(num1)
    number1 = float(num1)
    return number1


def inputNum2():
    num2 = input("Type your second number: ")
    is_valid = is_valid_integer(num2)
    while not is_valid or not float(num2):
        print("Please enter a valid number!")
        num2 = input("Type your second number: ")
        is_valid = is_valid_integer(num2)
    number2 = float(num2)
    return number2


def calculate():
    opInput = signInput()
    number_1 = inputNum1()
    number_2 = inputNum2()
    if opInput == "+":
        total = round(number_1 + number_2)
        return total
    elif opInput == "-":
        total = round(number_1 - number_2)
        return total
    elif opInput == "*":
        total = round(number_1 * number_2)
        return total
    elif opInput == "^":
        total = round(math.pow(number_1, number_2))
        return total


def output():
    total = calculate()
    print("total: " + "{:.2f}".format(total))


output()
