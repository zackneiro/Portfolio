def main() -> None:
    """
    Main function to demonstrate the dicntionary creating
    with dictionary comprehension.
    """
    dictionary: dict[int,str] = {x: ("even" if x % 2 == 0 else "odd") for x in range(1, 11)}
    print(dictionary)

main()