num = [3, 5, 1, 4, 2]
print(sorted(num))
print()
fruits = ["Banana", "Apple", "Orange", "Alpenliebe"]
print(sorted(fruits, key=len))
print()

# key wt our own function
def lastletter(name):
    return name[-1]

names = ['Peter', 'Jeff', "Thugga", 'Guwop']
result = sorted(names, key=lastletter)
print(result)
print()

def distance_from_zero(number):
    return abs(number)

numbers = [-10, 3, -2, 7, -5]

result = sorted(numbers, key=distance_from_zero)
print(result)
