def main() -> None:
    """
    Main function to demonstrate the work of the task's function.
    """
    print_table(10)
    print_table(5)
    print_table(-1)
    print_table(0)
    print_table(float('-inf'))
    print_table(float('+inf'))
    

def print_table(n: int) -> None:
    """
    Prints a multipliaction table up to n * n.
    
    Args:
        n(int): the value of the n * n formula.

    Returns:
        ValueError: if n <= 0 or n > 10 or n not int type.
    """
    if n <= 0 or not n or n > 10 or not isinstance(n, int):
        return ValueError (
            "n should be positive integer, \
             not less or equal to zero, and not greater than 10")

    for column in range(0, n):
        for row in range(1, n + 1):
            num = row * (column + 1)
            if num >= 10:
                print(f"{num} ", end="")
            else:
                print(f"{num}  ", end="")
        print()
    print()

main()