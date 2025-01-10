
def main() -> None:
    """
    Main function to demonstrate the work of 
    function which find th maximum value in 2D list.
    """

    test_list1: list[list[int]] = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
    test_list2: list[object] = []
    test_list3: list[list[object]] = [[], [], []]
    test_list4: list[list[object]] = [[], [1], [3]]
    test_list5: list[list[object]] = [[-213412], [-1], [0]]

    print(find_maximum_2d_list(test_list1))
    print(find_maximum_2d_list(test_list2))
    print(find_maximum_2d_list(test_list3))
    print(find_maximum_2d_list(test_list4))
    print(find_maximum_2d_list(test_list5))


def find_maximum_2d_list(nested_list: list[list[int | float]]) -> int | float:
    """
    Returns the maximum value of a 2D list elements if it's not empty.

    Args: 
        nested_list(list[list[int | float]]): the giving list to work with.
    
    Returns:
        int | float: the maximum value in the 2D list if it's not empty.
        None: if list or all sublists are empty.
        ValueError: 
            if at least one of the elements of sublist is not int or float.
    """   

    if not nested_list or not any(any(sublist) for sublist in nested_list):
        return None
    
    for sublist in nested_list:
        if not all(isinstance(element, (float, int)) for element in sublist):
            raise ValueError (
                "All the elements in the 2D list should be integer or float type.")
            
    return max(max(sublist) for sublist in nested_list if sublist)


main()