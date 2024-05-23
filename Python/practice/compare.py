from Python.practice.simple_calculator import get_int

def main():
    """
    Main function to excute the compare operations.
    """
    x = get_int("Enter the first number: ", min_value=-1000000, max_value=1000000)
    y = get_int("Enter the second number: ", min_value=-1000000, max_value=1000000)

    compare(x, y)


    def compare(x, y):
        """
        Function to compare two integers and print the result.
        """
        if x < y:
            print(f"{x} < {y}")
        elif x > y:
            print(f"{x} > {y}")
        elif x == y:
            print(f"{x} = {y}")
        else:
            print("Unxpected error")

        
    if __name__ == '__main__':
        main()