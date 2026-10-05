for row in range(5):
    for star in range(row + 1):
        print("*", end="")
    print()

#Right-growing triangle

for row in range(5):
    for _ in range(5 - row - 1):
        print(" ", end="")
    for star in range(row + 1):
        print("*", end="")
    print()

print()

#Inverse triangle
for row in range(5):
    for star in range(5 - row):
        print("*", end="")
    print()


#Right-growing inverse triangle
for row in range(5):
    for _ in range(row):
        print(" ", end="")
    for star in range(5 - row):
        print("*", end="")
    print()

print()

#Pyramid
for row in range(5):
    for _ in range(5 - row - 1):
        print(" ", end="")
    for star in range(2 * row + 1):
        print("*", end="")
    print()

print()

#Inverted pyramid
for row in range(5):
    for _ in range(row):
        print(" ", end="")
    for star in range(9 - (2 * row)):
        print("*", end="")
    print()

print()

#Diamond
for row in range(5):
    for _ in range(5 - row - 1):
        print(" ", end="")
    for star in range(2 * row + 1):
        print("*", end="")
    print()
#For bottom half: remove 1st line of inverse pyramid
for row in range(1, 5):
    for _ in range(row):
        print(" ", end="")
    for star in range(9 - (2 * row)):
        print("*", end="")
    print()

print()

#Inverse diamond - hourglass
#inverted pyramid
for row in range(5):
    for _ in range(row):
        print(" ", end="")
    for star in range(9 - (2 * row)):
        print("*", end="")
    print()
#for bottom part, pyramid but remove 1st row
for row in range(1, 5):
    for _ in range(5 - row - 1):
        print(" ", end="")
    for star in range(2 * row + 1):
        print("*", end="")
    print()

print()

#For hollow square
for row in range(5):
    for column in range(5):
        if row == 0 or row == 4 or column == 0 or column == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

#Hollow pyramid
for row in range(5):
    for column in range(9):
        if row == 4 or column == 4 - row or column == 4 + row:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

#Hollow diamond
#hollow pyramid +  inverse hollow pyramid without 1st row)
for row in range(5):
    for column in range(9):
        if row == 4 or column == 4 - row or column == 4 + row:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#inverse hollow pyramid w/o 1st row
for row in range(1, 5):
    for column in range(9):
        if column == row or column == 8 - row:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

#Hollow hourglass
#Inverted hollow pyramid + inverted pyramid w/o 1st row
for row in range(5):
    for column in range(9):
        if row == 0 or column == row or column == 8 - row:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#Inverted hollow pyramid w/o 1st row
for row in range(1, 5):
    for column in range(9):
        if row == 4 or column == 4 - row or column == 4 + row:
            print("*", end="")
        else:
            print(" ", end="")
    print()
