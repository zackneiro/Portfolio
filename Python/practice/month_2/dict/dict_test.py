from typing import Any

def main() -> None:
    dictionary_1 = {"a": 5, "b": 10}
    dictionary_2 = {"b": 20, "c": 30}

    print(merge_dict(dictionary_1, dictionary_2))


def merge_dict(dictA : dict[str, int], dictB: dict[str, int]) -> dict[str, int]:
    """
    This function will merge two dictionaries.
    If dictionary B has the same keys as A, then it sums
    their values 
    """
    if not dictA: # if dictA is empty, it will return dictB
        return dictB
    if not dictB:
        return dictA # if dictA is empty, it will return dictB
    
    merged = dictA.copy() # fresh dictionary to escaped unexpected behavior

    for key, value in dictB.items():
        if key in dictA.keys():
            merged[key] += value
        else:
            merged[key] = value

    return merged



main()