def countdown(n):
    if n < 0:  #base case tell program when to stop, else it keeps going till RecursionError
        return
    print(n)
    countdown(n - 1)   #recursive case where func calls itself w a smaller problem (n-1)
    print('Done', n)
countdown(4)             #create another call to same func but w diff value

print()

def countdown(n):
    if n == 0:
        return
    print('Down', n)
    countdown(n - 1)
    print('Up', n)
countdown(3)

print()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(3))
print(factorial(1))

print()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 2)
print(factorial(5))
# print(factorial(4))    keeps goin till RecursionError cos it never reaches base case as it skipped it

print()

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(0))

# a recursive function needs a base case that guarantee termination and a recursive step that solves correct smaller version of the problem

#RECURSION + A LIST
def recursive_sum(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])
print(recursive_sum([4, 7, 2]))