def main() -> None:
    """Main function to demonstrate the work of converting tuple to a list."""

    numbers: tuple[int, ...]= (10, 20, 30, 40)

    print(list(numbers))

main()