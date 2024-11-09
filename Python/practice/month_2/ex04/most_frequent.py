def main() -> None:
    some_list_int = [1, 2, 3, 4, 5, 1, 5, 6, 7, 1]
    some_list_str = ['duck', 'dog', 'cat', 'duck', 'dog', 'dog']
    
    print(most_frequent(some_list_int))

    print(most_frequent(some_list_str))

def most_frequent(object : list) -> any:
    count = {}
    for item in object:
        count[item] = count.get(item, 0) + 1

    frequent = float('-inf')
    
    for score in count.values():
        if score > frequent:
            frequent = score

    key_list = list(count.keys())
    val_list = list(count.values())

    print(count.values())

    position = val_list.index(frequent)
    return key_list[position]


main()