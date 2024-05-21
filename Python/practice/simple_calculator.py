def main():
    x = get_int("Enter the first inetger: ")
    y = get_int("Enter the second ingeter: ")
    choice = input("Choose your operation: +, -, /, %, *, //: ")
    # while user's choice is not valid, keep asking for a valid choice
    while valid_choice(choice) == False:
        print("Invalid choice")
        choice = input("Choose your operation: +, -, /, %, *, //: ")

    # perfom the chosen operation and display the result
    perform_operation(choice, x, y)

# function to get an integer for user, handling invalid input


def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Not an integer.Please enter a valid integer.")

# function to validate the user's choice of operation


def valid_choice(choice):
    options = ('+', '-', '/', '*', '%', '//')
    return choice in options

# function to perfom the chosen opertion on the given integers


def perform_operation(option, x, y):
    if option == '+':
        print(f"{x} + {y} = {x + y}")
    elif option == '-':
        print(f"{x} - {y} = {x - y}")
    elif option == '/':
        if y != 0:
            print(f"{x} / {y} = {x / y}")
        else: 
            print("Division by zero is not allowed")
    elif option == '%':
        print(f"{x} % {y} = {x % y}")
    elif option == '*':
        print(f"{x} * {y} = {x * y}")
    elif option == '//':
        if y != 0:
            print(f"{x} // {y} = {x // y}")
        else:
            print("Division by zero is not allowed")


if __name__ == "__maim__":
    main()