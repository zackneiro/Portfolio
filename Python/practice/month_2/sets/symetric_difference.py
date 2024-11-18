from typing import Any

def main() -> None:
    print(find_symetric_difference({1, 2, 3, 4}, {1, 15, 534, 4}))
    print(find_symetric_difference({15, 4, 123, -1}, {1, 15, 534, 4}))
    print(find_symetric_difference({}, {1, 15, 534, 4}))
    print(find_symetric_difference({15, 4, 123, -1}, {}))
    print(find_symetric_difference({-1, -1, -1, -1}, {-5, -5, -1, -4}))
    print(find_symetric_difference({0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}))


def find_symetric_difference(set_1 : set[Any], set_2 : set[Any]) -> set[Any]:

    return set_1.symmetric_difference(set_2)


main()