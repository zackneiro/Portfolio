def main() -> None:
    """Main funciton to demonstrate the 
    work of string validation using all()."""
    print(valid_string(["HELLO", "WORLD", "PYTHON"]))
    print(valid_string(["Hello", "WORLD", "PYTHON"]))
    print(valid_string([]))


def valid_string(strings : list[str]) -> bool:
    """
    Validates the strings with specified condition.
    In this case is strings are uppercase.

    Args:
        string_list(list[str]): list of strings.
    
    Returns:
        True: If the list is empty or all string are uppercase.
        Flase: If at least one string is not uppercase.
    """
    if not all(isinstance(word, str) for word in strings):
        raise ValueError("All the elements in input list should be string type.")
    
    return all(word.isupper() for word in strings)


main()