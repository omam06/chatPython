numbers = [12, 5, 8, 21, 30, 17]

count = 0
#program that prints only the even numbers
for number in numbers:
    if number % 2 == 0:
        print(number)
        count += 1
print("Total even numbers:", count)


'''follow up questions:
why does line 5 correctly identify even no.(what % does)
if its empty list, what will be printed? will it crash, why?
how to print odd num instead with slight change in code
'''