# input_helpers.py
def input_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except Exception as ex:
        print("Error, numbers are not float")
        return
    return num1, num2
