def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "%": modulo
}

def calculator():
    print("Welcome to the calculator program!")
    num1 = float(input("What's the first number?\n"))
    continue_calc = True
    while(continue_calc):
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from the line above:\n")
        calc_op = operations[operation]
        num2 = float(input("What's the second number?\n"))
        result = calc_op(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        num1 = result
        continue_calc = input("keep calculating? (y/n)\n") == "y"
    print("Goodbye!")

calculator()