# To find the biggest number in a sequence/list
numbers = [7, 13, 9, 17, 15, 22]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)


# To count how many even numbers are in a list
numbers = [3, 8, 4, 9, 10]
count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
print(count)


# To count how many odd numbers are in a list
numbers = [4, 7, 12, 15, 20, 17, 23]
count = 0
for number in numbers:
    if number % 2 == 1:
        count = count + 1
print(count)