from typing import Any

def main() -> None:
    set_1 = {1, 2, 3, 4, 5, 6, 7}
    set_2 = {1, 2, 3, 4, 10, 21, 123, 153}
    print(find_common(set_1, set_2))


def find_common(set_1 : set[Any], set_2 : set[Any]) -> set[Any]:

    return set_1.intersection(set_2)

main()