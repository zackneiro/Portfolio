import os

def get_input():
    """
    Function to get input values for comparison.
    """
    if os.getenv('CI', 'false').lower() == 'true' or os.getenv('TESTING', 'false').lower() == 'true':
        x = int(os.getenv('INPUT1', 0))
        y = int(os.getenv('INPUT2', 0))
    else:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
    return x, y

def main():
    """
    Main function to perform comparison of two numbers.
    """
    print("Starting the compare script...")
    x, y = get_input()
    result = is_even_or_odd(x, y)
    print(result)

def is_even_or_odd(x, y):
    """
    Function to determine if two numbers are even or odd.
    """
    def even_or_odd(n):
        return "even" if n % 2 == 0 else "odd"
    
    return f"{x} is {even_or_odd(x)} and {y} is {even_or_odd(y)}"

if __name__ == '__main__':
    main()
