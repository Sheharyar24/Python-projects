"""
Creating a basic calculator
"""

def menu():
    '''Display the options to the user'''
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def addition(a, b):
    '''Add two numbers'''
    ans = a + b
    return f"\n{a} + {b} = {ans} \n"

def subtraction(a, b):
    '''subtract two numbers'''
    ans = a - b
    return f"\n{a} - {b} = {ans} \n"

def multiplication(a, b):
    '''multiply two numbers'''
    ans = a * b
    return f"\n{a} * {b} = {ans} \n"

def division(a, b):
    '''divide two numbers'''
    ans = a / b
    return f"\n{a} / {b} = {ans} \n"

def solve(q):
    '''Used to do the operation'''
    if q == '+':
        print(addition(num1, num2))
    elif q == '-':
        print(subtraction(num1, num2))
    elif q == '*':
        print(multiplication(num1, num2))
    elif q == '/':
        print(division(num1, num2))


while True:
    question = input("Enter the type of problem you wish to solve (or type 'quit' to exit): ")

    if question == "quit":
        break
    
    try:
        question = question.split()
        num1 = int(question[0])
        num2 = int(question[2])
        symbol  = question[1]
        solve(symbol)
    except ValueError:
        print("Cannot enter a string, try '2 + 2'\n")
    except IndexError:
        print("Please enter 2 numbers only!, eg. '1 + 1'\n ")
    except ZeroDivisionError:
        print("Cannot divide by zero!\n")

print("Goodbye!")
