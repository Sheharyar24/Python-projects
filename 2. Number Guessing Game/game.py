'''Number Guessing Game'''

import random

def num():
    '''Generates a random number'''
    x = random.randint(1,10)
    return x

# Generate and store a number
y = num()
print(y) # for reference to see what the number is

# The number of guesses the user has
COUNT = 3
TRIES = COUNT + 1

print("Welcome to the Guessing Game!")
print(f"You have {COUNT} guesses!\n")


while True:
    guess = int(input("Guess the number (between 1 - 10): "))

    if guess == y:
        print(f"Well done!, You guessed it in {TRIES - COUNT} tries")
        break
    if COUNT == 1:
        print("You are out of attempts!")
        break
    else:
        COUNT -= 1
        print(f"You have {COUNT} remaining attempts")
