# calculator.py
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2


def get_function_for_operation(operation):
    match operation:
        case '+':
            return add
        case '-':
            return subtract
        case '*':
            return multiply
        case '/':
            return divide
