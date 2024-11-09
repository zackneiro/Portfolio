def main():
    print(list_sum([]))
    print(list_sum([100]))
    print(list_sum([-21, -12, -512]))
    print(list_sum([12, 4324, 123]))
    print(list_sum([4, 23, 1]))
    print(list_sum([-21, 500, -512]))

    print(sum([]))



def list_sum(numbers_list : list[int]) -> int:
    total = 0
    for number in numbers_list:
        total += number
    return total

def test_list_sum() -> None:
    assert list_sum([1, 2, 3, 4, 5, 6]) == 21
    assert list_sum([2, 25, 62, 12, 53]) == 154
    assert list_sum([-1, 0, 123000, -200]) == 122799


main()