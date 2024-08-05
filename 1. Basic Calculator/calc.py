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
    if q == 1:
        print(addition(num1, num2))
    elif q == 2:
        print(subtraction(num1, num2))
    elif q == 3:
        print(multiplication(num1, num2))
    elif q == 4:
        print(division(num1, num2))    


while True:
    menu()
    question = input("Enter the type of problem you wish to solve (or type 'quit' to exit): ")

    if question == "quit":
        break

    question = int(question)

    if question > 4 or question < 1:
        print("\nInvalid Input, try again")
    else:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

    solve(question)

print("Goodbye!")
