def get_student():
    name = input("Name: ").strip().title()

    email = input("Email: ").strip().lower()

    language = input("Favorite Language: ").upper()
    return name, email, language

def display_profile(name, email, language):
    print("---------- user profile ----------".upper())
    print("Name: ", name)
    print("Email: ", email)
    print("Language: ", language)
    print("Total characters in Name: ", len(name))

def validate_email(email):
    if "@" in email:
        return "Email is valid"
    else:
        return "Invalid Email"

def process_student():
    name, email, language = get_student()
    display_profile(name, email, language)
    result = validate_email(email)
    return result

result = process_student()
print(result)


