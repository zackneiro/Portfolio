from Python.practice.simple_calculator import get_int
import os


def main():
    """
    Main function to excute the compare operations.
    """
    print("Starting the compare script...")  # Debug print
    if os.getenv('CI', 'false').lower() == 'true':
        x = int(os.getenv('INPUT1', 0))
        y = int(os.getenv('INPUT2', 0))
    else:
        x = get_int("Enter the first number: ")
        y = get_int("Enter the second number: ")

    result = is_even_or_odd(x, y)
    print(result)


def is_even_or_odd(x, y):
    def even_or_odd(n):
        return "even" if n % 2 == 0 else "odd"
    
    return f"{x} is {even_or_odd(x)} and {y} is {even_or_odd(y)}"
            
        
if __name__ == '__main__':
    main()