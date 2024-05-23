from cs50 import get_int
import os


def main():
    """
    Main function to perform factorial calculations.
    Depending on the environment, it either takes user input or reads from environment variables.
    """
    print("Starting the factorial calculation script...")  # Debug print

    # Check if the script is running in a CI environment
    if os.getenv('CI', 'false').lower() == 'true':
        n = int(os.getenv('INPUT', 0))
    else:
        # Prompt the user to enter an integer
        n = get_int("Please enter an integer: ")

    # Calculate the factorial of the input number
    result = factorial_calculation(n)

    # Print the result
    print(f"Factorial of number {n} is {result}")


def factorial_calculation(n):
    """
    Function to perform factorial calculation using recursion.
    
    Args:
        n (int): The integer for which the factorial is to be calculated.
        
    Returns:
        int: The factorial of the input number. Returns 1 for non-positive integers.
    """

    # Base case: factorial of 0 or negative numbers is 1
    if n <= 0:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    return n * factorial_calculation(n - 1)


if __name__ == '__main__':
    main()