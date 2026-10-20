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