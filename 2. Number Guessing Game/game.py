'''Number Guessing Game'''

import random

class InvalidNumber(Exception):
    '''Used when the user enters a number outside the range'''

def num():
    '''Generates a random number'''
    x = random.randint(1,10)
    return x

def play():
    '''Makes everything inside the function so that it can be played again'''
    # Generate and store a number
    y = num()

    # The number of guesses the user has
    count = 3
    tries = count + 1

    print("\nWelcome to the Guessing Game!")
    print(f"You have {count} guesses!\n")


    while count > 0:
        try:
            guess = int(input("Guess the number (between 1 - 10): "))
            if guess < 1 or guess > 10:
                raise InvalidNumber
        except InvalidNumber:
            print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a number!")

        if guess == y:
            print(f"Well done!, You guessed it in {tries - count} tries")
            break
        else:
            count -= 1

        if guess < y:
            print("Too low!")
        else:
            print("Too high!")
        
        if count > 0:
            print(f"You have {count} remaining attempts\n")
        else:
            print(f"You're out of attempts!, the number was {y}")

while True:
    play()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for playing!")
        break
