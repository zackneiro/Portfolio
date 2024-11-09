def main():
    print(find_second_largest([1, 2, 3, 4, 5, 6]))
    print(find_second_largest([25, 12, 1, 423, 324, 123]))
    print(find_second_largest([]))
    print(find_second_largest([-1, -51, -20, -32]))
    print(find_second_largest([-100, 23, 0, 1]))
    print(find_second_largest([1]))
    


def find_second_largest(list_numbers : int) -> int:
    if len(list_numbers) == 1:
        print("Only one number in the list.")
        return 
    elif len(list_numbers) == 0:
        print("List is empty.")
        return
    largest = float('-inf')
    second_largest = float('-inf')

    for number in list_numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

    if second_largest == float('-inf'):
        print("All elements are the same, no second largest.")
        return
    
    return second_largest


main()