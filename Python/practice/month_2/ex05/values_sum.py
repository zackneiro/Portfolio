def main() -> None:
    print(values_sum({"a": 10, "b": 20, "c": 30}))


def values_sum(object_dict : dict[str, int]) -> int:
    return sum(object_dict.values())


main()