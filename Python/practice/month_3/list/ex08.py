def main() -> None: 
    """
    Main function to demonstrate the work of converting 
    list of tuples to the one list.
    """

    pairs: list[tuple[int, int]] = [(1,2), (3, 4), (5, 6)]

    new_list: list[int] = [item for pair in pairs for item in pair]
    print(new_list)


main()