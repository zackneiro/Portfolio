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
    Calling all functions from here
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
                show_history()  # program will print the current history of operations
            case 4:
                print("Thank you for using our service and goodbye!")
                exit() # will exit the program
            
    

def greeting() -> None:
    """
    This block prints the greet message.
    """
    print("\nHi and welcome to basic calculator!",
          "Here are the operations I can perforom: ",
          " 1 - Basic calculations between two numbers.",
          " 2 - Data process of list of numbers. ",
          " 3 - Show your history of calulcation's totals.",
          " 4 - To exit calculator", sep="\n")


def ask_for_choice() -> int:
    """
    This block gets the main menu choice and validate it.
    """
    choice = 0
    choice = get_number("What'd be your choice? Please, enter from 1 to 4: ")
    while choice < 1 or choice > 4:
        choice = get_number("Please, enter a valid integer between 1 and 4: ")
    return choice

def get_number(promt : str ="") -> int:
    """
    Fucntion to gets a valid interger from user.
    
    Args:
    text : str ="" Optionally can accept a string
    """
    print(promt, end="")
    while True:
        try:
            return float(input())
        except ValueError:
            print("Please write a valid number: ", end="")


def get_string(*promt, separ=" ") -> str:
    """
    Function gets a valid string from user

    Args: 
    promt : str . Accepts an optional argument strint, standart =""
    """
    while True:
        try:
            for text in promt:
                print(text, sep="", end=separ) 
            return input().lower()
        except ValueError or TypeError:
            print("Please, write a valid string: ", end="")


def show_history(promt : str ="", in_history_assigning : int = 0) -> None:
    """
    Shows history of calculations

    Args: 
    promt : str - accepts string as custom message from user. Standard - "" 
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
    Block that begins the basic calculations
    and allows to follow the logic of block
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
    This block should return the result from number's containers
    I don't know the amount of coming numbers
    So, I will use variable-length argument *numbers
    Then I will ask the user for an opertaion choice,
    I will use the same function of choosing operation, 
    But I will add there one more choice
    Then I will define another function, where I already will proceed actcual
    operation,
    Then I will store result and append it to history.
    """
    print("\nThis block is data proccessing")
    operation = ask_choice_operation(choosing_opeartion=1)
    numbers = get_tuple_int("Please, enter a set of nubmers to use in opertaion: ")
    print(numbers)
    perform_operation_data(operation, numbers)
    


def get_tuple_int(promt : str) -> tuple[int]:
    while True:
        try:
            numbers = get_string(promt)
            return tuple(int(x) for x in numbers.split())
        except ValueError:
            print("Invalid input. Please try again.2")


def ask_choice_operation(choosing_opeartion : int = 0) -> str:

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
    Function assigns value to integer in basic_calculation block

    Args: 
    promt : str - accepts a cutsom string from user, standard = ""
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
    History value is one of the result in during previous calculations 
    """
    if len(history) == 0:
        number = 0
        number = get_number("History is empty, please enter interger yourself: ")
        return number
    elif len(history) == 1:
        show_history("This is a current history:", 1)
        return next(iter(history.values()))
    else:
        show_history("This is a current history:", 1)
        choice = get_string("Please enter a valid \
                            operation from history (e.g. '1 + 1')")
        while choice not in history.keys():
            choice = get_string("Invalid operation. Try again.")
        return history.get(choice)
    

def yes_or_no_chocie(*promt : str) -> int:
    """
    Returns user's choice depending on user's input
    yes returns 1
    no returns 2
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