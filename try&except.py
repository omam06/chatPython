try:
    number = int(input("Enter number: "))
    print(number * 2)
except:
    print("Not a number")


try:
    print(32 / 0)
except:
    print("Something went wrong!")
    