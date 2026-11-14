age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative")

print()

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount 
try:
    new_balance = withdraw(5000, 7000)
    print(f"New balance: {new_balance}")
except ValueError as e:
    print(e)

print()
# re-raising an exception.
try:
    number = int("hello")

except ValueError:
    print("Something went wrong!")
    try:
        raise                 #re-raises originl valueerror so as to send the same exception back up for another part of the program to handle it.
    except ValueError:                  #if no exception to handle 2nd raise, twill print full error msg then crash program at that point
        print("Second handler caught the error")

print("Program continues")

# EXERCISE
def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    if a < 0 or b < 0:
        raise ValueError("Negative numbers are not allowed.")
    return a / b

def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list")
    for number in numbers:
        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError("Expected a number")
    else:
        return sum(numbers) / len(numbers)
