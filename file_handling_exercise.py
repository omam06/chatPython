import os

user_input = input("Enter text: ").strip()
if os.path.exists("my_notes.txt") and os.path.getsize("my_notes.txt") > 0:
        content = f"\n{user_input}"
else:
        content = user_input

with open("my_notes.txt", "a") as file:                     # instead of separate with open in if & else blocks, do it once outside both blocks
        file.write(content)
print()

# Task
filename = input("Enter filename: ").strip()
try:
    with open(filename, "r") as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print("Oooppsss! File Does not exist.")
else:
    print("File read successfully!")       
finally:
    print("Operation completed.")