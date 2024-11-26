def main() -> None:
    """
    Main function to demonstarte work of reversing dinctionary
    using the dictionary comprehension.
    """
    original: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    print(reverse_dictionary(original))


def reverse_dictionary(dictionary : dict[str, int]) -> dict[int, str]:
    """
    Reverses the giving dictionary.
    Swaping the keys and values positions,
    where key become value and value become keys.

    Args:
        dictionary (dict[str, int]): 
            Giving dictionary, where key is string and value is int format.

    Returns:
        dict[int, str]: swaped dictionary.
    """

    return {value: key for key, value in dictionary.items()}


main()