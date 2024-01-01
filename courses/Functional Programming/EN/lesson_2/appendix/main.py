# main.py
import calculator
import console.display_helpers as disp_help
from console import input_helpers as inp_help

def main():
    while True:
        disp_help.display_menu()
        operation = input("Enter your choice: ")

        numbers = input_helpers.input_numbers()
        if not numbers:
            continue
        num1, num2 = numbers  # unpacking

        operation_function = calculator.get_function_for_operation(operation)
        try:
            result = operation_function(num1, num2)
            display_result(operation, num1, num2, result)
        except Exception as ex:
            print(ex)

        continue_calculation = input("Do you want to continue calculating? (Y/N): ")
        if continue_calculation.lower() == "n":
            break


if __name__ == "__main__":
    main()
# main.py
