def ascii_sum(string : str) -> int:
    check = ("a", "e", "i", "o", "u")
    print(sum(ord(char) for char in string.lower() if char in check))

ascii_sum("Hello")