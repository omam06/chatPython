again = "yes"
while again == "yes":
    try:
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
    except:
        print("Enter valid numbers!")

    operation = input("choose operation (/, +, *, -): ")

    if operation == "+":
        print("The answer is:", num1 + num2)
    elif operation == "-":
        print("The answer is:", num1 - num2)
    elif operation == "/":
        try:
            print("The answer is:", num1 / num2)
        except:
            print("cannot divide by 0")
    elif operation == "*":
        print("The answer is:", num1 * num2)
    else:
        print("Invalid operation")
    again = input("Run another calculation? (yes/no) ").lower()
print("So long, sucker!")