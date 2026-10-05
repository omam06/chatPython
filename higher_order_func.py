# passing a func as arg. to another func
def greet():
    print("Tay Keith, fucc these niggas up!")

def symbiosis():
    print("Ajb hustlers")

def cazulee(func):
    func()
cazulee(greet)

print()

# instead of manually choosing a function, let it decide when to run it
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 5, 5))
print(calculate(multiply, 5, 5))

print()

# functions can be stored  in a list too

def double(x):
    return x * 2
def triple(x):
    return x * 3
operations = [double, triple]
print(operations[0] (5))
print(operations[1] (4))

print()

# making a function to return a function

def create_greeting():
    def greet():
        print("Hello Thugga")
    return greet
my_function = create_greeting()
my_function()
