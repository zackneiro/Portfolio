def main() -> None:
    """Main function to demonstrate the work of transform function."""

    original = {"apple": 15, "banana": 25, "cherry": 30, "date": 10}

    print(transform_dict(original, 20))


def transform_dict(
            dictionary: dict[str, int], filter : int
            ) -> dict[str, int]:
    """
    Filters and transforms keys which are greater than filter-number.

    Args:
        dictionary(dict[str, Any]): 
            accepts a dictionary where key are in string format
            and values are in integer/float formats.
    """
    if not all(
        isinstance(k, str) and isinstance(v, (int, float))
        for k, v in dictionary.items()
    ):
        raise TypeError("All keys must be strings and valuse must be int or float.")

    return {k.upper(): v for k, v in dictionary.items() if v > filter}

main()