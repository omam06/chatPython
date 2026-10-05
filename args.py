# Making a function take an arbitrary number of arguments
def add(*args):
    print(args)
add(10, 20, 30)

print()

def add(*args):
    print(args)
add()

print()

# To make it add items
def add(*args):
    total = 0
    for number in args:
        total += number
    return total
print(add(10, 20, 30, 40))

print()

def add(*args):
    count = 0
    for number in args:
        count += 1
    print(count)
add(28, 38, 29, "1y", 16, 67, 28)

print()

def add(*args):
    largest = args[0]
    for number in args:
        if number > largest:
            largest = number
    print(largest)
add(20, 50, 37)

print()

