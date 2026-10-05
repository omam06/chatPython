names = ["Peter", "James", "Sarah", "Alice"]
print(names[3])

print()

numbers = [1, 2, 3, 4, 5]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

print()

numbers = [1, 2, 3, 4, 5]
for x in numbers:
    if x % 2 == 1:
        print(x)

        