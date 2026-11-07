# Files allow our programs to store information beyond a single execution. When you close a program, variables disappear.
file = open("my_notes.txt", "w")
file.write("I am learning Python File Handling.")
file.close()

file = open("my_notes.txt", "a")
file.write(" And I'm having a great time.")
file.close()

file = open("my_notes.txt", "r")
content = file.read()
print(content)
file.close()