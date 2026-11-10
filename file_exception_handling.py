# An exception is an error that occurs while a program is running and interrupts its normal execution. Rather than allowing the program to crash, we can handle the exception
try:
    with open("unknown_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Sorry, that file does not exist.")

finally:                                            #Used to close files too, but since we used context manager, no need to manually close here.
    print("Operation completed.")
print()

# Introducing multiple except blocks
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:                                                   #Only runs if try does
    print("Result:", result)
finally:                                                #Always runs at end of the program
    print("Operation completed.")
print()

# Working with file paths and directories - python won't find a file that isn't in cwd, if only filename was given, so include path
# with open("my_notes.txt/my_notes.txt", "r") as file:
#     content = file.read()

import os

print(os.getcwd())   #tells us dir python currently using
# C:\Users\OMALE\Desktop\chatPython
os.chdir("Study_Projects")     # uses a relative path, so it starts from cwd. Changes to another dir inside cwd 
print(os.getcwd())     # ---> C:\Users\OMALE\Desktop\chatPython\Study_Projects
os.chdir("..")      #back to chatPython
# Checking if a path exists
print(os.path.exists("my_notes.txt"))       #can check 4 both files and dir. atekes absolute path too.
print(os.path.isfile("my_notes.txt"))
print(os.path.isdir("my_notes.txt"))
print()

# os.listdir() - lists the contents of a directory
content_s = os.listdir("Study_Projects")
print(content_s)