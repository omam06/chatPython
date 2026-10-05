try:
    num = int(input("Enter a number: "))
    print(100 / num)
except:
    print("Cannot divide by zero!")

for row in range(5):
    for _ in range(row):
        print(" ", end="")
    for star in range(9, 0, -2):
        print("*", end="")
    print()

