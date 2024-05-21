def main():
    x = get_int("x: ")
    y = get_int("y: ")
    option = input("Choose your operation: "
                   "+, -, /, %, *, //: ")
    operations(option, x , y)
    return

def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except:
            ValueError
            print("Not an integer.")

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