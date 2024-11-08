"""
Basic calculator

This module provide functionalities for performing basic arithmetic
calculations and processing data on lists of numbers. It includes
operations such as addition, subtraction, multiplication, division,
and advacned data processng function like finding the average,
mainumn, and minimum of a set of numbers.

Fuctions:
    - main(): Main entry point for the calculator program.
    - basic_calculation(): Handle arithmetic operations between two numbers.
    - proceed_data(): Processes a list of numbers for advanced calculations.
    - show_history(): Displays a history of calculations.
    - assign_history_value(): Assigns a value, allowing use of previous results.
    - get_integer(): Gets valid integer from user

Classes:
    - None in this module.

Usage example:
    - Run main() to start calculator:

    >>>main()   
"""


from numpy import average as avg

history = {}
def main():
    """
    Entry point for the calculator program, whic prompts user to select
    an option and directs them to the corresponding functionality

    Options:
        1 - Perfrom basic calculations between two numbers.
        2 - Process a list of numbers for advanced calculations.
        3 - Display history of calculations.
        4 - Exit the program.

    Returns: 
        None
    """
    choice = 0
    while choice != 4:
        greeting() # function to greet the user in the start of work
        choice = ask_for_choice() # returns 1 length digigt of user's choice
        match choice: # match the user's choice with cases 
            case 1:
                basic_calculation() # program proceeds to basic calculations block
            case 2:
                proceed_data() # program proceeds to data process block
            case 3:
                history_work()  # program will print the current history of operations
            case 4:
                print("Thank you for using our service and goodbye!")
                exit() # will exit the program
            
    

def greeting() -> None:
    """Print a welcome message to the user."""

    print("\nHi and welcome to basic calculator!",
          "Here are the operations I can perforom: ",
          " 1 - Basic calculations between two numbers.",
          " 2 - Data process of list of numbers. ",
          " 3 - Show your history of calulcation's totals.",
          " 4 - To exit calculator", sep="\n")


def ask_for_choice() -> int:
    """
    Asks user for a choice to choose an option from the main().

    Returns: 
        int: A valid choice (1-4) representing the selected menu option.
    """
    choice = 0
    choice = get_number("What'd be your choice? Please, enter from 1 to 4: ")
    while choice < 1 or choice > 4:
        choice = get_number("Please, enter a valid integer between 1 and 4: ")
    return choice

def get_number(promt : str ="") -> float:
    """
    Gets a valid float number from the user.
    
    Args:
        prompt (str): The custom message displayed to the user.
    
    Returns:
        float: A valid numeric input prvided by the user
    """
    print(promt, end="")
    while True:
        try:
            return float(input())
        except ValueError:
            print("Please write a valid number: ", end="")


def get_string(*promt, separ=" ") -> str:
    """
    Gets a valid string from user.

    Args: 
        promt (tuple[str]): the tuple of custom strings, by default is " " 

    Returns:
         str: valid string
    """
    while True:
        try:
            for text in promt:
                print(text, sep="", end=separ) 
            return input().lower()
        except ValueError or TypeError:
            print("Please, write a valid string: ", end="")


def history_work(promt : str ="", in_history_assigning : int = 0) -> None:
    """
    Shows history of calculations.

    Args: 
        promt (str): The custom message displayed to the user.
        in_history_assigning (int): indicator shows that we are 
            in history value assigning (0 by default)

    Returns:
        None
    """
    if len(history) == 0: 
        print("\nThe history is empty.")
    elif in_history_assigning == 0:
        print(promt)
        for operation, result in history.items():
            print(operation, "=", result, sep=" ")
    elif in_history_assigning == 1:
        print(promt)
        for perform, result in history.items():
            print(perform, "=", result, sep=" ")

def basic_calculation() -> None:
    """
    Handles basic arithmetic calculations between two numbers.
    
    Prompts the user to select or enter two numbers and an operation.
    The result of the operation is displayed and saved to history.

    Returns:
        None.
    """
    number_1 = assign_value_int("Do you want to use one of the last results as",
                                "the value of first number? Write \"yes\" or \"no\": ")
    number_2 = assign_value_int("Do you want to use one of the last results as"
                                "the value of second number? Write \"yes\" or \"no\": ")
    operation = ask_choice_operation()
    perform_operation_basic(operation, number_1, number_2)
    print(number_1, number_2, operation)


def proceed_data() -> None:
    """
    Handles the data proceed.
    Same as basic_calcualtions allows to follow the logic of this option.
    """
    print("\nThis block is data proccessing")
    operation = ask_choice_operation(choosing_opeartion=1)
    numbers = get_tuple_int("Please, enter a set of nubmers to use in opertaion: ")
    print(numbers)
    perform_operation_data(operation, numbers)
    


def get_tuple_int(promt : str) -> tuple[int]:
    """
    Gets tuple of integers.

    Args:
        promt (str): the custom promt.
    
    Returns: 
        tuple (int): tuple of integers.
    """
    while True:
        try:
            numbers = get_string(promt)
            return tuple(int(x) for x in numbers.split())
        except ValueError:
            print("Invalid input. Please try again.2")


def ask_choice_operation(choosing_opeartion : int = 0) -> str:
    """
    Block that validates the user choice of operations
    Depending on the block he is current in.

    Args:
        choosing_operation (int): the integer that 
        by default is 0 if functon called from basic_calculation(),
        has value 1 is called from proceed_data(). 
    
    Returns:
        str: valid operation
    """

    valid_operations_basic={"+", "%", "/", "-", "*", "//"}
    valid_operations_data={"+", "avg", "min", "max"}

    if choosing_opeartion == 0:
        operation_basic = get_string("What operation you would like to peroform: ",
                                "Please, enter for your choice:",
                                "* - to multiply", "+ - to sum",
                                "/ - to divide", "- - to substracy",
                                "% - for modulo opertaion",
                                "// - for floor division", separ="\n")
        while operation_basic not in valid_operations_basic:
            operation_basic = get_string("Please, choose valid operation from the list:",
                                    "* - to multiply", "+ - to sum",
                                    "/ - to divide", "- - to substracy",
                                    "% - for modulo opertaion", "// - for floor division", separ="\n")
        return operation_basic
    elif choosing_opeartion == 1:
        operation_data = get_string("What you would like the calculator to perform?",
                                "Please, enter for your choice:",
                                "+ - sum of all numbers",
                                "avg - average for all nubmers",
                                "max - to find maximum number",
                                "min - to find minimum number", separ="\n")
        while operation_data not in valid_operations_data:
            operation_data = get_string("What you would like the calculator to perform?",
                                "Please, enter for your choice:",
                                "+ - sum of all numbers",
                                "avg - average for all nubmers",
                                "max - to find maximum number",
                                "min - to find minimum number", separ="\n")
        print("ready")
        return operation_data
        


def perform_operation_basic(operation : str, n1 : int, n2 : int) -> None:
    """
    Performs basic operations between two numbers.

    Args:
        operation (str): valid operation.
        n1 (int): first number ín operation.
        n2 (int): second number in operation. 

    Returns:
        None, but it appends the result and operation itself
        to global variable "hitsory", which stores the result during the work
        as key-value pair in set.
    """

    perform = {"+" : lambda n1, n2 : n1 + n2,
               "-" : lambda n1, n2 : n1 - n2,
               "*" : lambda n1, n2 : n1 * n2,
               "/" : lambda n1, n2 : n1 / n2 if n2 != 0 
               else "Division by zero is not allowed!",
               "%" : lambda n1, n2 : n1 % n2 if n2 != 0 
               else "Modulo by zero is not allwoed!",
               "//": lambda n1, n2 : n1 // n2 if n2 != 0 
               else "Floor division by zero is not allowed!"}

    result= perform[operation](n1, n2)
    operation_key = f"{n1} {operation} {n2}"
    if isinstance(result, str):
        print(result)
    else:
        if isinstance(result, float):
            result = round(result, 2)
            print(f"{n1} {operation} {n2} = {result}")
        else:
            print(f"{n1} {operation} {n2} = {result}")
        history[operation_key] = result


def perform_operation_data(operation : str, numbers : tuple[int]) -> None:
    """
    Performs data process opertaions using tuple of numbers

    Args:
        operation (str): valid operation
        numbers (tuple[int]): tuple of integers

    Returns:
        Nothing, but it appends the result and operation itself
        to global variable "hitsory", which stores result during work
        as a key-value pair in set
    """

    print("This is operation_data_perform!")
    perform = {"+" : sum(numbers),
                "avg": avg(numbers),
                "max" : max(numbers), 
                "min" : min(numbers)}

    result = perform[operation]
    if isinstance(result, float):
        result = round(result, 2)
    operation_key = f"{operation}{numbers}"
    history[operation_key] = result
    print(operation_key,"=",result)



def assign_value_int(*promt : str) -> int:
    """
    Gets an integer depending on user choice.
    It can append history value if user wants that and history is not empty,
    by calling assign_history_value().
    Otherwise it will call get_number() and assign custom value.

    Args:
        *promt (str): The tuple of strings.
    
    Returns:
        int : the valid integer or history value depending on user.
    """
    choice = 0
    choice = yes_or_no_chocie(*promt)
    if choice == 1 and history != None:
        return assign_history_value()
    else:
        return get_number("In this case, please, enter a valid integer:  ")

def assign_history_value() -> int:
    """
    Assigns history value to the variable.

    History value is one of the result in during previous calculations.
    If history is empty, it will ask user to enter a valid integer.
    If history is not empty, but has one item, then it assigns it automatically.
    Otherwise it will diplay history, asks user to enter the key e.g. '1 + 1'
    and program will assign result of that historical operation.

    Returns:
        int: a valid integer from the history of calculations.

    """
    if len(history) == 0:
        number = 0
        number = get_number("History is empty, please enter interger yourself: ")
        return number
    elif len(history) == 1:
        history_work("This is a current history:", 1)
        return next(iter(history.values()))
    else:
        history_work("This is a current history:", 1)
        choice = get_string("Please enter a valid \
                            operation from history (e.g. '1 + 1')")
        while choice not in history.keys():
            choice = get_string("Invalid operation. Try again.")
        return history.get(choice)
    

def yes_or_no_chocie(*promt : str) -> int:
    """
    Returns user's choice depending on user's input.

    Args:
        *promt (tuple[str]): custom promt treated as a tuple of strings
    
    Returns:
        int (1): if user entered 'yes'
        int (2): if user entered 'no'
    """
    answers = ("yes", "no")
    answer = get_string(*promt)
    while answer.lower() not in answers:
        answer = get_string("Please, enter \"yes\" or \"no\": ").lower()
    if answer == "yes":
        return 1
    elif answer == "no":
        return 2
    



main()