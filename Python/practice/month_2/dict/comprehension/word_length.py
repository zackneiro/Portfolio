def main() -> None:
    """
    Main function demonstrates the creating dictionary 
    with dictionary comprehension, where key is the word
    and value is its length.
    """
    words: list[str] = ["apple", "banana", "cherry", "date"]
    dictionary: dict[str, int] = {word: len(word) for word in words}
    print(dictionary)


main()