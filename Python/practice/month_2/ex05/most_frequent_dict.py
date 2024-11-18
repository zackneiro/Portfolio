def main() -> None:
    print(count_word_frequency("apple banana apple orange banana apple"))


def count_word_frequency(string : str) -> dict[str, int]:
    new_dict = dict()
    for word in string.split():
        new_dict[word] = new_dict.get(word, 0) + 1
    
    return new_dict
        



main()