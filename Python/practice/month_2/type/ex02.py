def main() -> None:
    """Main function to demonstrate the work of list_to_dict()."""

    test = [(2 , 2), ("b", 2), ("c", 3)]
    print(list_to_dict(test))



def list_to_dict(list_object: list[tuple[str, int | float]]) -> dict[str, int]:
    """
    Converts list of tuples to the dctionary,
    where tuples are structed in key-value pair,
    where key is string and value is int or float type.

    Args:
        list_object(list[tuple[str, int | float]): A list of tuples.
    
    Returns:
        dict[str, int]: Converted dictionary.
        None if giving list is empty.
    """

    if not list_object:
        raise ValueError ("You trying to pass an empty list. Please, try again.")
    
    list_object = dict(list_object)
    
    list_object = {str(key) : int(value) for key, value in list_object.items()}

    return list_object
            

main()