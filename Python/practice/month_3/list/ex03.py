def main() -> None:
    """
    Main function to demonstrate the work
    of extracting keys from dictionary with list().
    """
    fruit_prices: dict[str, int] = {"apple" : 100, "banana" :  50, "cherry" : 200}

    print(list(fruit_prices.keys()))


main()