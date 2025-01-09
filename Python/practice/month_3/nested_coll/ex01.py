def main() -> None:
    """
    Main function to demonstrate the work of
    summing all elements in a nested list.
    """

    data: list[list[int]] = [[1, 2, 3], [4, 5], [6]]
    
    total: int = 0

    for sublist in data:
        total += sum(sublist)

    print(total)


main()