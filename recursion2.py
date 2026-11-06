def reach_zero(n):
    if n == 0:
        return "Stopped"

    return reach_zero(n - 1)


print(reach_zero(3))

def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n - 1)
    print("Back:", n)

count_down(3)

#Write a recursive function count_down_list(lst) that returns the number of items in a list, without using len()
def count_down_list(lst):
    if lst == []:
        return 0
    return 1 + count_down_list(lst[1:])

print(count_down_list([10, 20, 30, 40]))
print()

#Write a recursive function called sum_list(lst) that returns the sum of all numbers in a list, without using sum() or loops.
def sum_list(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([5, 2, 8]))
print()

#Write a recursive function called count_occurrences(lst, target) that returns how many times target appears in lst.
def count_occurrences(lst, target):
    if lst == []:
        return 0
    elif lst[0] == target:
        return 1 + count_occurrences(lst[1:], target)
    else:
        return count_occurrences(lst[1:], target)

print(count_occurrences(["a", "b", "a"], "a"))
print()

#Write a recursive function called count_evens(lst) that returns the number of even integers in a list.
def count_evens(lst):
    if lst == []:
        return 0
    elif lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:])
    else:
        return count_evens(lst[1:])

print(count_evens([1, 2, 4, 7, 8]))
print()

#Write a function called max_recursive(lst) that returns the largest number in a non-empty list, without using max() or loops.
def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    
    largest = max_recursive(lst[1:])
    if lst[0] > largest:
        return lst[0]
    else:
        return  largest
print(max_recursive([15, 4, 21, 8]))
print()

#Write a recursive function called first_index(lst, target) that returns the index of the first occurrence of target in the list. If the target isn't present, return -1.
def first_index(lst, target):
    if lst == []:
        return -1
    elif lst[0] == target:
        return 0
    #result = first_index(lst[1:], target)
    elif first_index(lst[1:], target) == -1:
        return -1
    else:
        return 1 + first_index(lst[1:], target)

print(first_index([4, 7, 2, 7, 4, 2, 12], 4))
print()

#write a recursive function that finds the last occurrence of a target in a list.
def last_index(numbers, target):
    if numbers == []:                   #base case
        return -1
    result = last_index(numbers[1:], target) 
    if result != -1:
        return result + 1
    elif numbers[0] == target:
        return 0
    else:
        return -1
print(last_index([4, 7, 2, 7], 7))
print(last_index([4, 7, 2, 7], 2))
print(last_index([4, 7, 2], 9))
print(last_index([], 5))
print()

#write a recursive function that return a new list containing the items in reverse order.
def reverse_list(numbers):
    if numbers == [] or len(numbers) == 1:                       #base
        return numbers
    versed = reverse_list(numbers[1:])           #take out 1st item and recursively reverse remaining list
    item1 = numbers[0]
    return versed + [item1]                                  #put it in a list. its int rn (+ combine both lists)
print(reverse_list([1, 2, 3, 4, 5]))
print()

def sum_list(numbers):
    if numbers == []:
        return 0
    return numbers[0] + sum_list(numbers[1:])
print(sum_list([1, 3, 5]))
print()

#Write a recursive function called is_palindrome(numbers) that checks whether a list reads the same forwards and backwards.
def is_palindrome(numbers):
    if len(numbers) <= 1:
        return True
    elif numbers[0] != numbers[-1]:
        return False
    else:
        return is_palindrome(numbers[1:-1])
print(is_palindrome([1, 3, 1, 7, 1]))
print(is_palindrome([21, 17, 12, 17, 21]))
print(is_palindrome([9, 13, 9]))

def mystery(n):
    if n == 0:
        return 0

    return n + mystery(n - 1)

print(mystery(4))