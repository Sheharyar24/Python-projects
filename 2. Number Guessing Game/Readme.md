# Number Guessing Game
#### A game where the computer randomly selects a number, and the user has to guess it within a certain number of attempts.

## Game Requirements

### 1. Random Number Generation:
+ The program should generate a random number within a specified range (e.g., 1 to 100).
+ The range can be predefined or set by the user at the start of the game.


### 2. User Input:
+ The program should prompt the user to guess the number.
+ Input should be validated to ensure it's an integer within the specified range.

### 3. Guess Evaluation:
+ The program should compare the user's guess to the generated number.
+ It should inform the user if the guess is too high, too low, or correct.

### 4. Guess Limit:
+ The program should limit the number of guesses (e.g., 10 attempts).
+ After each guess, the program should display the number of remaining attempts.

### 5. Winning & Losing Condition:
+ If the user guesses the correct number within the allowed attempts, the program should congratulate the user and end the game.
+ If the user fails to guess the correct number within the allowed attempts, the program should reveal the correct number and end the game.

### 6. Replay Option:
+ After the game ends (win or lose), the program should offer the user the option to play again.
+ If the user chooses to replay, the game should reset with a new random number.
----

### Additional Features (Optional):
+ Allow the user to set the range of numbers at the start of the game.
+ Track and display the number of games played and the number of wins/losses.
+ Implement a scoring system based on the number of attempts used to guess the number correctly.