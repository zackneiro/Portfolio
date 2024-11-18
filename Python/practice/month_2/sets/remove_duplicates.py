from typing import Any

def main() -> None:
    print(remove_duplicates([1, 1, 1, 2, 3, 4, 5]))
    print(remove_duplicates([0, 0, 0, 0]))
    print(remove_duplicates([-1, -1, -1, -1]))
    print(remove_duplicates([]))
    print(remove_duplicates([1]))


def remove_duplicates(object : list[Any]) -> list[Any]:
    if len(object) == 0:
        return object
    
    new_set = set()
    new_list = []

    for item in object:
        if item not in new_set:
            new_list.append(item)
            new_set.add(item)

    return new_list


main()