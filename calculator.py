while True:
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))

    op = input("Please choose which operation you want to do: 'a' for addition; 's' for subtraction; 'm' for multiplication; 'd' for division; 'md' for modulus; 'fd' for floor division; 'e' for exponents: ")

    if op == "a":
        print(num1 + num2)

    elif op == "s":
        print(num1 - num2)

    elif op == "m":
        print(num1 * num2)

    elif op == "d":
        print(num1 / num2)

    elif op == "fd":
        print(num1 // num2)

    elif op == "md":
        print(num1 % num2)

    else:
        print(num1 ** num2)

    choice = input("\nDo you want to perform an operation again. Click 'Y' if you want to and any other key to end the program. ")

    if choice != "Y":
        break
    else:
        continue