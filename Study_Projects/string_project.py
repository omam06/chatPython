FullName = input("Name: ").strip().title()

Email = input("Email: ").strip().lower()

Language = input("Favorite Language: ").upper()

print("---------- user profile ----------".upper())
print("Name: ", FullName)
print("Email: ", Email)
print("Language: ", Language)
print("Total characters in Name: ", len(FullName))
if "@" in Email:
    print("Email is valid.")
else:
    print("Invalid Email!")
