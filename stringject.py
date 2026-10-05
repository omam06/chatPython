name = input("Enter your name: ").title()
email = input("Enter your email address: ").lower()
language = input("Your favorite language: ").upper()
total_xters = (len(name))

print("-------- uSeR PrOfILe --------".upper())
print("Name:", name)
print("Email:", email)
print("Language:", language)
print("Total characters in Name:", total_xters)
if "@" in email:
    print("Email is valid")
else:
    print("Invalid email!")
