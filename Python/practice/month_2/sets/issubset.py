from typing import Any

def main() -> None:
    print(check_subset({1, 2, 3}, {1, 2, 3, 4, 5}))
    print(check_subset({"read", "write", "delete"}, {"read", "write"}))


def check_subset(set_1 : set[Any], set_2 : set[Any]) -> bool:
    return set_1.issubset(set_2)


main()