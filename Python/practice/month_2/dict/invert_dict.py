def main() -> None:
    """
    Main function to demonstrate inevrtation of dictionary
    """
    dict_test = {"a" : 1, "b" : 2, "c" : 3}
    print(invert_dict(dict_test))


def invert_dict(dict_org : dict[str, int]) -> dict[int,str]:
    """
    Function inverts key - values of original dictionary.

    Assumes that all values in the input dictionary are unique.

    Args:
        dict_org (dict[str, int]): Original dictionary
    
    Returns:
        dinct_invert (dict[str, int]): Inverted dictionary
        dctionary is empty, returns an empty dictionary
    """

    if not dict_org:
        return dict_org

    dict_invert = dict()

    for key, value in dict_org.items():
        dict_invert[value] = key

    return dict_invert

main()