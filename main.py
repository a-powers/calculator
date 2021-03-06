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
    "/": divide,
}


def calculator():

    num_1 = int(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation from the line above.")
        num_2 = int(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit.") == 'y':
            num_1 = answer
        else:
            continue_calculation = False
            calculator()

calculator()
calculator()
