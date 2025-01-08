def main() -> None:
    """
    The main function to demonstrate the work of 
    coverting set to the list without saving original order.
    """

    unique_numbers: set[int] = {4, 8, 15, 16, 23, 42}
    
    print(list(unique_numbers))

    empty_set: set[int] = set()
    not_unique_numbers: set[int] = {4, 4, 4, 8, 121, 23, 8, 8, 23}

    print(list(empty_set))
    print(list(not_unique_numbers))


main()