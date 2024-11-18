def main() -> None:
    """
    Main function to demonstrate counting common keys.
    """
    dict_1 = {"a": 5, "b": 10, "c": 15}
    dict_2 = {"b": 20, "c": 30, "d": 40}

    print(count_common_keys(dict_1, dict_2))


def count_common_keys(
        dict1 : dict[str, int], 
        dict2 : dict[str, int]
    ) -> int:

    """
    Function counts common keys of two dictionaries.

    Args:
        dict1 (dict[str, int]): First dictionary.
        dict2 (dict[str, int]): Second dictionary.

    Returns:
        int : Amount of common keys.
    """

    if not dict1:
        return dict2
    if not dict2:
        return dict1
    
    return len(set(dict1) & set(dict2))

main()