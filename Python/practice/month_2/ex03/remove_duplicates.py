def main() -> None:
    some_list = []
    new_list = remove_duplicates(some_list)
    print(new_list)
    test_remove_duplicates()

def remove_duplicates(old_list : list[int]) -> list[int]:
    if len(old_list) == 0:
        return old_list
    new_list = []
    for number in old_list:
        if number not in new_list:
            new_list.append(number)

    return new_list

def test_remove_duplicates() -> None:
    assert remove_duplicates([]) == []
    assert remove_duplicates([-1, -2, -3, -1, -4, -3]) == [-1, -2, -3, -4]
    assert remove_duplicates([-1, -2, -3, -4]) == [-1, -2, -3, - 4]
    assert remove_duplicates(['inf', '-inf', 'inf']) == ['inf', '-inf']
    assert remove_duplicates([1.23, 1.23, 1.23, 1.23]) == [1.23]

    print("All test passed.")


main()