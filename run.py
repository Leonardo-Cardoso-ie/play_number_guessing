import random

# Minimum number
# Create a variable for a minimum number and insert input
min_number = int(input('Please enter minimum number: '))
 
# Maximum number 
# Create a variable for the maximum number and insert input
max_number = int(input('Please enter maximum number: '))

# Random number to guess
# Create a variable rand_number
rand_number = random.randint(min_number, max_number)

# NUmber of chances
chances = 3 

""" 
Prompt user to guess number
Create a while loop
"""
while chances >= 0:
    chances -= 1
    guess = int(input(f'Guess a number between {min_number} and {max_number}:')) # our min and max number run here
# Tell us if we guessed to high or low

# Tell us if we are right or wrong

# Prompt us if win or loose

# Keep score and give us an option to retry