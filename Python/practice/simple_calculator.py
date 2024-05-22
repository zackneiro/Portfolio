def main():
    """
    Main function to execute the calculator operations.
    """
    x = get_int("Enter the first integer: ", min_value=-1000000, max_value=1000000)
    y = get_int("Enter the second integer: ", min_value=-1000000, max_value=1000000)
    choice = get_operation_choice("Choose your operation: +, -, /, %, *, //: ")

    # perfom the chosen operation and display the result
    perform_operation(choice, x, y)


def get_int(prompt, min_value=None, max_value=None, error_message="Not an integer. Please enter a valid integer."):
    """
    Prompt the user to enter an integer within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter an integer between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print(error_message)


def get_operation_choice(prompt, valid_options={'+', '-', '/', '*', '%', '//'}):
    """
    Prompt the user to choose a valid operation.
    """
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid choice.")


def perform_operation(option, x, y):
    """
    Perform the chosen operation on the given integers and display the result.
    """
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 or a != 0 else "Division by zero is not allowed.",
        '%': lambda a, b: a % b if b != 0 or a != 0 else "Division by zero is not allowed.",
        '//': lambda a, b: a // b if b != 0 or a != 0 else "Division by zero is not allowed."
    }
    if option in operations:
        result = operations[option](x, y)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{x} {option} {y} = {result}")  # Check if result is an error message
    else:
        print("Invalid operation")


if __name__ == '__main__':
    main()