x = int(input("x: "))
y = int(input("y: "))


option = input("Choose your operation: "
               "+, -, /, %, *, //: ")
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