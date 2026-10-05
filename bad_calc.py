again = "yes"
while again == "yes":
        try:
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
        except:
             print("enter valid numbers!")

        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
             print("The answer is:", num1 + num2)
        elif operation == "-":
             print("Result:", num1 - num2)

        elif operation == "/":
             try:
                  print("The answer is:", num1 / num2)
             except:
                  print("Cannot divide by 0")

        elif operation == "*":
             print("The answer is:", num1 * num2)

        else:
             print("Invalid operation!")

        again = input("Do another calculation? (yes/no): ").lower()
print("Goodbye, MOTHERFUCKER!")
