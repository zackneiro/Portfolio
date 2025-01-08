def main() -> None:
    """Main function to demonstrate the work of Str_list_to_int_list()."""

    print(Str_list_to_int_list(["1", "2", "hello"]))


def Str_list_to_int_list(list_1 : list[str]) -> list[int]:
    """
    Function converts strings of numbers to integers.
    Works only if string represents some number.

    Args:
        list_1(list[str]): Giving list of numbers, strings.

    Returns:
        Converted list of integers.
    """
    if not list_1:
        print("The giving list is empty, please try again.")
        return list_1
    
    new_list = []

    for element in list_1:
        try:
            int(element)
        except ValueError:
            print(
                f"Element '{element}' doesn't represent",
                  "an integer and cannot be converted."
            )
        else:
            new_list.append(int(element))

    if not new_list:
        print("No elements were converted successfully. Please, try again.")
    return new_list


main()