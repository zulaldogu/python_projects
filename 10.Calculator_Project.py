def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
import art


def calculator():
    print(art.logo)
    first_number = float(input("What is the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    next_number = float(input("What is the next number?: "))
    result = operations[operation](first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")
    restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while restart == "y":
        first_number = result
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))
        result = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while restart == "n":
        print("\n" * 20)
        first_number = float(input("What is the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))
        result = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
