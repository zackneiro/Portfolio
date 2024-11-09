from typing import Any

def main() -> None:
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {6, 7, 8, 9, 10}
    print(union_sets(set_1, set_2))



def union_sets(set_1 : set[Any], set_2 : set[Any]) -> set[Any]:

    return set_1.union(set_2)


main()