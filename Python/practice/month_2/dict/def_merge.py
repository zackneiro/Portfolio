def main() -> None:
    def_dict = {"a" : 0, "b" : 0, "c" : 0}
    inpt_dict = {"a" : 5, "b" : 10}

    print(merge_dict(def_dict, inpt_dict))


def merge_dict(
        default_dict: dict[str, int], 
        inpt_dict : dict[str, int]
    ) -> dict[str, int]:
    """
    Merges two dictionaries.

    Args:
        default_dict (dict[str, int]): The default dictionary
        input_dict (dict[str, int]): The dictionary whose valuse overried defaults.

    Returns:
        dict[str, int]: A merged dictionary containing all keys. 
    """
    
    merged = default_dict.copy()

    for key, value in inpt_dict.items():
        merged[key] = value

    return merged


main()