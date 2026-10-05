again = "yes"
while again == "yes":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Enter valid numbers!")

    operation = input("Choose operation (+, -, /, *, //): ")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "/":
        try:
            print(num1 / num2)
        except:
            print("Cannot divide by 0 !")
    elif operation == "*":
        print(num1 * num2)
    elif operation == "//":
        try:
            print(num1 // num2)
        except:
            print("Cannot divide by 0 !")
    else:
        print("Invalid operation")
    again = input("Do another calculation? (yes/no): ").lower()
print("Goodbye!")
    