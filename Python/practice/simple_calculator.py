def main():
    x = int(input("x: "))
    y = int(input("y: "))
    option = input("Choose your operation: "
                   "+, -, /, %, *, //: ")
    operations(option, x , y)
    return


def operations(option, x, y):
    if option == '+':
        print(x + y)
    elif option == '-':
        print(x - y)
    elif option == '/':
        print(x / y)
    elif option == '%':
        print(x % y)
    elif option == '*':
        print(x * y)
    elif option == '//':
        print(x // y)


main()