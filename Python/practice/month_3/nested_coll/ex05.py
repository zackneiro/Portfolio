from typing import  List

def main() -> None:
    """
    Main functuon to demonstrate the work of
    function, which generates 2D list.
    """
    print(generate_2D_list(-1))

    


def generate_2D_list(n : int) -> List[List[int]]:
    """
    Generates 2D list, where:
      - First row contains numbers from 1 to n,
      - Second row contains numbers n+1 to 2n, and so on.

    Args:
        n(int): number of rows (and the size of each row).

    Returns:
        List[List[int]]: A 2D list with `n` rows.

    Raises:
        ValueError: If 'n' is not a positive integer or equal zero.

    Example:
        >>> generate_2D_list(3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    # Argument validation.
    if not isinstance(n, int) or n <= 0 or not n:
        raise ValueError("The n should be a valid integer, not equal zero.")

    # Local variable declaration.
    my_list: list[list[int]] = list()

    # Creating 2D list.
    end = n + 1
    start = 1
    for row in range(0, n):
        my_list.append([num for num in range(start, end)])
        start = end
        end += n

    return my_list


main()