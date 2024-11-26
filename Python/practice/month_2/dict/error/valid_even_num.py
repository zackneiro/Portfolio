def main() -> None: 
    """Main function to demonstrate the work of all()."""
    print(valid_even_num([2, 4, 6, 8]))
    print(valid_even_num([1, 2, 4, 6]))
    print(valid_even_num([]))


def valid_even_num(num_list : list[int]) -> bool:
    """
    Validates the numbers.
    Args:
        object(Any[iny]): a giving iterable object.
    Returns:
        True, if all numbers are even, and if list is empty.
        False, if at least one number is odd.
    """

    if not all(isinstance(num, int) for num in num_list):
        raise ValueError("List should contains only integers.")

    return all(num % 2 == 0 for num in num_list)


main()