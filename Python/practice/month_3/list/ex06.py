def main() -> None:
    """
    Main function to demonstrate the work of converting str to list.
    Two different strings combines together,
    and converted to the list.
    """
    
    string1: str = "data"
    string2: str = "science"

    print(list(string1 + string2))


main()