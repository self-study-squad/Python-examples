# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again 
# until the guess is correct, on successful guess, 
# user will get a "Well guessed!" message, and the program will exit.

import random
target_num = random.randint(1,10)
guess_num = int(input('Please input your first guess: '))
while target_num != guess_num:
    if target_num > guess_num:
        guess_num = int(input('You guess wrong! Please guess higher: '))
    elif target_num < guess_num:
        guess_num = int(input('You guess wrong! Please guess lower: '))
print('Well guessed!')