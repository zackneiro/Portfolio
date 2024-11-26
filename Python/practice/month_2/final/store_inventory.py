# That is a start inventory.
inventory: dict[str, dict[str : int, str : int]] = {
    "apple": {"price": 1.0, "stock": 50},
    "banana": {"price": 0.5, "stock": 100},
    "cherry": {"price": 2.0, "stock": 25}
}

"""
    New ideas.
    - I can save inventory in text file after finsihing work and open that 
        in the start. Will do it later, when I will work with files.
"""


def main() -> None:
    """
    Main function to follow the logic of this project.
    This program will show work of basic inventory management system.
    The system will:
        1. Accept a dictionary of products.
        2.Perform the following tasks:
            - Check Validity of the Inventory.
            - Add a New Product.
            - Calculate Total Stock Value.
            - Find Low Stock Products.
            - Generate a Summary.
    """

    choice: int = 0

    # This is a menu, from where user will choose what he wants to do.

    while choice != 6:
        choice = get_choice_menu(
            "Hello! Welcome to store_inventory.",
            "Now you are in the main menu:",
            " 1 - To add new product.",
            " 2 - To calculate total sotck value.",
            " 3 - To find low stock product.",
            " 4 - To generate summary.",
            " 5 - To exit program.", 
            "Please, choose from 1 to 5:"
            )
        print(choice)
        match choice:
            case 1:
                add_new_prdouct()
            case 2:
                calculate_total_stock_value()
            case 3:
                find_low_stock()
            case 4:
                generate_summary()
            case 5:
                print("The program is about to close...")
                exit()


def get_choice_menu(*prompt: tuple[str]) -> int:
    """
    This function asks user for choice and validate it.
    
    Args:
        promt(str): A custom developer's message.
    
    Returns:
        Valid integer from 1 to 6.
    """
    while True:
        try:
            for text in prompt:
                print(text, sep="")
            choice = int(input())
        except ValueError:
            print(
                "You entered not the valid integer.", 
                "Please, enter the number from 1 to 5."
            )
        else:
            return choice
        



def check_validity():
    """
    This block runs program that ensures all product names are strings,
    prices are postive floats, and stock is a non-negative integer.
    """


def add_new_prdouct():
    """
    This block runs program that adds new valid product.
    """


def calculate_total_stock_value():
    """
    This block runs program that calculate total stock value.
    """


def find_low_stock():
    """
    This block runs program that finds low stock in the inventory.
    """


def generate_summary():
    """
    This block runs program that generates summary of the inventory.
    """


main()