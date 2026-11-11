# An exception is an error that occurs while a program is running and interrupts its normal execution. Rather than allowing the program to crash, we can handle the exception
try:
    with open("unknown_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Sorry, that file does not exist.")

finally:                                            #Used to close files too, but since we used context manager, no need to manually close here.
    print("Operation completed.")
print()

# Introducing multiple except blocks
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:                                                   #Only runs if try does
    print("Result:", result)
finally:                                                #Always runs at end of the program
    print("Operation completed.")
print()
