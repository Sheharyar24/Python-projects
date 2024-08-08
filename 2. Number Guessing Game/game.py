'''Number Guessing Game'''

import random

class InvalidNumber(Exception):
    '''Used when the user enters a number outside the range'''

def num():
    '''Generates a random number'''
    x = random.randint(1,10)
    return x

# Generate and store a number
y = num()

# The number of guesses the user has
COUNT = 3
TRIES = COUNT + 1

print("Welcome to the Guessing Game!")
print(f"You have {COUNT} guesses!\n")


while COUNT > 0:
    try:
        guess = int(input("Guess the number (between 1 - 10): "))
        if guess < 1 or guess > 10:
            raise InvalidNumber
    except InvalidNumber:
        print("Please enter a number between 1 and 10")
    except ValueError:
        print("Please enter a number!")

    if guess == y:
        print(f"Well done!, You guessed it in {TRIES - COUNT} tries")
        break
    else:
        COUNT -= 1

        if guess < y:
            print("Too low!")
        else:
            print("Too high!")
        
        if COUNT > 0:
            print(f"You have {COUNT} remaining attempts\n")
        else:
            print(f"You're out of attempts!, the number was {y}")
