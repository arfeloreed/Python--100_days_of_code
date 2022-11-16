from art import logo
import os

# math operations in a calculator
# addition
def add(n1, n2):
    return n1 + n2

# subtraction
def minus(n1, n2):
    return n1 - n2

# multiplication
def multiply(n1, n2):
    return n1 * n2

# division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    calculator_active = True
    while calculator_active:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        repeat = input(f"Type 'y' to continue calculating with {answer}, type "
                                    "'n' to start a new calculation or type 'e' "
                                    "to exit.:").lower()
        if repeat == "y":
            num1 = answer
        elif repeat == "n":
            calculator_active = False
            os.system("clear")
            calculator()
        else:
            calculator_active = False
            os.system("clear")

calculator()
