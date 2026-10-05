for i in range(1, 4):
    print("Outer:", i)

    for j in range(1, 3):
        print("Inner:", j)

def introduce(name, age):
    print(name)
    print(age)

introduce(22, "Thugga")

def greet(name):
    print("Hello", name)
person = "Keith"
greet(person)

print()

def hello():
    print("Hi")
x = hello()
print(x)

print()
# ** is raise to power
def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3, 3))