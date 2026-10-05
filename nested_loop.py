for i in range(2):
    for j in range(3):
        print(i, j)

print()

for i in range(3):
    print("Start")

    for j in range(2):
        print("Hello")

    print("End")
    print()

for i in range(3):
    for j in range(4):
        print("*")
    print()

print()

for i in range(5):
    print("*", end="")

print()
print()

#Square
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

print()

for i in range(4):
    print("#", end=" ")

print()
print()

# Star aligning from left
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()

print()

# Star aligning from right
for i in range(4):
    # First, for spaces
    for j in range(4 - i - 1):
        print(" ", end="")
    # Now, for stars
    for j in range(i + 1):
        print("*", end="")
    print()

print()

#For inverse star from left
for i in range(4):
    #To reduce stars by 1
    for j in range(4 - i):
        print("*", end="")
    #For spaces
    for j in range(4 - i + 1):
        print(" ", end="")
    print()

print()

#For inverse star from right
for i in range(4):
    for j in range(4 - 1 + 1):
        print("*", end="")
    for j in range(4 - 1):
        print(" ", end="")
    print()

print()

for row in range(1, 5):
    for star in range(row):
        print ("*", end="")
    print()

