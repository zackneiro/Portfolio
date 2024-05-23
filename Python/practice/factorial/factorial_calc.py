from cs50 import get_int
import os


def main():
    """
    Main function to perform factorial calculations.
    """
    print("Starting the compare script...")  # Debug print
    if os.getenv('CI', 'false').lower() == 'true':
        n = int(os.getenv('INPUT', 0))
    else:

        n = get_int("Please enter an integer: ")

    result = factorial_calculation(n)
    print(f"Factorial of number {n} is {result}")


def factorial_calculation(n):
    """
    Faction to perform factorial calculations by making a recurseive call
    """
    
    if n <= 0:
        return 1
    
    return n * factorial_calculation(n - 1)


if __name__ == '__main__':
    main()