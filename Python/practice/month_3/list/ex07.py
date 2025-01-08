def main() -> None:
    """
    Main function to demonstrate the work
    of converting the generator to the list.
    """
    gen = (x ** 2 for x in range(1, 6))

    print("Squares of numbers from 1 to 5:", list(gen))
    print(list(gen)) # edge case to show that generator can only be used once.


main()