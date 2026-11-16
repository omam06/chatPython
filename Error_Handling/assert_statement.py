# Assert is used to check whether a condition is true.

age = 21
assert age >= 18, "Must be atleast 18 to enter"
print("Access granted!")
print()

temperature = 40
try:
    assert temperature <= 35, "Temperature is too high!"
except AssertionError as e:
    print(e)
print("Continuing program...") 
print()

# Assert inside a function
def double_numbers(numbers):
    x2 = []
    for number in numbers:
        x2.append(number * 2)
    assert len(x2) == len(numbers), "Number of items do not match"
    return x2

print(double_numbers([2, 4, 6]))
print()

# Validating a function's assumptions
def calculate_average(numbers):
    assert numbers != [], "List of numbers is empty"
    return sum(numbers) / len(numbers)
try:
    print(calculate_average([]))
except AssertionError as e:
    print(e)