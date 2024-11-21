def main() -> None:
    """
    Main fucntion to demonstrates the filtering the existing
    dictionary with dictionary comprehension.
    """
    prices: dict[str, int] = {"apple": 15, "banana": 25, "cherry": 30, "date": 10}

    new_prices: dict[str, int] = update_prices(10, prices, 20)

    print(new_prices)


def update_prices(
        percent : int, prices : dict [str, int],
        condition_number : int, precision : int = 2
    ) -> dict[str, float]:
    """
    Updates prices with dictionary comprehension.
    
    Args:
        percent (int): percent to increase the prices.
        prices (dict[str, int]): dictionary of current prices.
        condition_number (int): line upper what prices will be updated.
        precision (int): Optional allows to choose the amount 
                         of digits in the final price after comma.

    Returns:
        returns giving dictionary if it is empty.
        returns dictonary of updated prices.
    
    """
    if not prices or percent < 1 or condition_number < 0 :
        raise ValueError("Invalid input: Check prices, percent, and condition_number.")

    return {name: round(price * (1 + percent / 100), precision) for name, price in prices.items() \
                if price > condition_number}

main()