import os


def main():
    """
    Main function to execute the calculator operations.
    """
    if 'CI' in os.environ:
        # Use default values if running in CI environment
        x = int(os.getenv('X_VALUE', 0))
        y = int(os.getenv('Y_VALUE', 0))
        choice = os.getenv('CHOICE', '+')
    else:
        x = get_int("Enter the first integer: ", min_value=-1000000, max_value=1000000)
        y = get_int("Enter the second integer: ", min_value=-1000000, max_value=1000000)
        choice = get_operation_choice("Choose your operation: +, -, /, %, *, //: ")

    # perfom the chosen operation and display the result
    perform_operation(choice, x, y)
    

def get_int(prompt, min_value=-1000000, max_value=1000000, error_message="Not an integer. Please enter a valid integer."):
    """
    Prompt the user to enter an integer within the specified range.
    """
    if os.getenv('CI', 'false').lower() == 'true':
        # Use environment variables for CI
        value = int(os.getenv(prompt.split()[-1].upper(), 0))
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Please enter an integer between {min_value} and {max_value}.")
            return min_value
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter an integer between {min_value} and {max_value}.")
        except ValueError:
            print(error_message)


def get_operation_choice(prompt, valid_options={'+', '-', '/', '*', '%', '//'}):
    """
    Prompt the user to choose a valid operation.
    """
    if os.getenv('CI', 'false').lower() == 'true':
        # Use environment variables for CI
        return os.getenv('CHOICE', '+')
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid choice.")


def perform_operation(option, x, y):
    """
    Perform the chosen operation on the given integers and return the result.
    """
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Division by zero is not allowed",
        '%': lambda a, b: a % b if b != 0 else "Division by zero is not allowed",
        '//': lambda a, b: a // b if b != 0 else "Division by zero is not allowed"
    }

    result = operations[option](x, y)
    if isinstance(result, str):  # Check if result is an error message
        print(result)
        return result
    else:
        print(f"{x} {option} {y} = {result}")
        return f"{x} {option} {y} = {result}"


if __name__ == '__main__':
    main()