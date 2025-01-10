def main() -> None:
    """
    Main function to demonstrate the work of the function
    which accepts 2D list and returns the sum of all elements.
    """

    nested_list1: list[list[int]]= [[1, 2, 3], [4, 5, 6]]
    half_empty_list: list[list[int]] = [[], [1, 2, 3], []]
    empty_list: list [list[object ]]= [[]]
    float_int_list: list[list[float | int]] = [[1, 3.4, 2], [], [5.01, -23, 4]]
    only_negative_values_list: list[list[int | float]] = [
        [-1, -2.123, -3], # 1st sublist
        [-4, -0.12312423423, -6, -7], # 2nd sublist
        [] # empty list
    ]


    # tests
    print(sum_2dlist_elements(nested_list1))
    print(sum_2dlist_elements(half_empty_list))
    print(sum_2dlist_elements(empty_list))
    print(sum_2dlist_elements(float_int_list))
    print(sum_2dlist_elements(only_negative_values_list))




def sum_2dlist_elements(
        object_list_2d : list[list[int | float]]) -> list | int | float:
    """
    Returns the sum of the nested list elements.

    Args:
        object_list_2d(list[list[int | float]]): 2D list (list of lists)

    Returns:
        Empty list if parameter is empty.
        Sum of the elements of the list.
    """    

    if not object_list_2d: 
        return object_list_2d
    
    # 2 check to validate the elements in the nested list.
    # I accept the list with empty sub lists, if there are not empty lists.

    for sublist in object_list_2d:
        for element in sublist:
            if not isinstance(element, (int, float)):
                raise ValueError ("All the elements should be valid integer of float.")
    
    total: int = 0
    for sublist in object_list_2d:
        total+= sum(sublist)

    if isinstance(total, float):
        total = round(total, 2)

    return total

main()