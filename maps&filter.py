# applies given function to every item in a list/tu
def double(m):
    return m * 2
numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(list(result))

print()

numbres = (1, 2, 3, 4)
result = map(lambda x: x ** 2, numbres)
print(tuple(result))

print()

# filter keep only items that meet a condition

scores = [48, 28, 59, 76, 82]
result = filter(lambda q: q > 70, scores)
print(list(result))

print()

names = ['John', 'Theophilus', 'James', 'Jane', 'Tom']
result = filter(lambda name: len(name) > 4, names)
print(list(result))

print()

# combining both

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x * 10, filter(lambda x: x > 3, numbers))
print(list(result))

print()

def demok(p):
    return p ** 3
umbre = (4, 8, 12)
reta = map(demok, umbre)
print(tuple(reta))
