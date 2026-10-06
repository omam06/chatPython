# #1
# okpa, pepsi, bag = 700, 500, 100
# total_cost = okpa + pepsi + bag
# print(f'The Total cost is: {total_cost}')

# #2
# average = total_cost / 3
# print(f'The Average score is: {average:.2f}')

# #3
# score = 47
# if score > 50:
#     print('Student Passed')
# else:
#     print('Student Failed')

#4
# == is used to compare 2 values to check if they are equal. Whereas, 
# =, called an assignment operator - is used to assign value to variables and other items

# #5
# programming_languages = ['Python', 'Golang', 'JavaScript']
# print('Python' in programming_languages)

print()

# #Assignment 3 — Strings

# • Ask for a full name.
FullName = input('What is your full name? ').strip()

# • Print it in uppercase and lowercase.
print(FullName.upper())
print(FullName.lower())

# • Count characters.
number_of_xters = len(FullName)

# • Create a personalized f-string message.
print(f'{FullName} has {number_of_xters} characters')   

# • Extract first and last names.
name = FullName.split()
print(name)

print('First Name:', name[0])
print('Last Name:', name[1])