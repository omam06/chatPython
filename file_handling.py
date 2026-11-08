# Files allow our programs to store information beyond a single execution. When you close a program, variables disappear.
file = open("my_notes.txt", "w")
file.write("""I am learning Python.
File Handling is interesting.""")
file.close()

file = open("my_notes.txt", "a")
file.write("\nAnd I'm having a great time. \nMaking progress as well.")
file.close()

file = open("my_notes.txt", "r")
content = file.read()
print(content)
file.close()
print()

 #with is context manager, closes file by default after indentation
with open("my_notes.txt", "r") as file:          
    first_line = file.readline()                #readline retrieve line by line from top
print(first_line)
print()

#readlines() retrieves all remaining lines (if you already read some) and returns them as a list of strings
with open("my_notes.txt", "r") as file:
    lines = file.readlines()
print(lines)
print()

with open("my_notes.txt", "r") as file:
    first = file.readline()
    second = file.readline()
    third = file.readline()
    fourth = file.readline()
    fifth = file.readline()
print(repr(fifth))                   #show actual representation instead of empty output, show '' (empty str)
print()

# File pointers and seek. The position at which python last stopped reading is called file pointer/position
# Assuming you've called 2 lines with readline(), the pointer moves past the 2nd line to beginning of 3rd line. If you wan to go back to line1 and read the file again, use seek()
# file.seek(0) moves the file pointer to position 0; the beginning of the file. 

with open("my_notes.txt", "r") as file:
    line1 = file.readline()
    print(first)
    print(file.tell())

    print()
    file.seek(0)
    line = file.readline()
    print(line)

    file.seek(0)
    content = file.read()
    print(content)

# tell() gives current position of the pointer
ga = "I am learning Python."
print(len(ga))
print()

with open("my_notes.txt", "r") as file:
    line1 = file.readline()

    print(repr(line1))
    print(len(line1))
    print(file.tell())     #tell adds 1 (for \r) to len(including newline) cos each line end as \r\n
print()

with open("my_notes.txt", "r") as file:
    line1 = file.readline()
    position = file.tell()

    file.seek(0)
    file.seek(position)                            #take pointer to end of 1st line, so 2nd line prints

    print(file.readline())               
print()


#looping through a file to print each line w/o using readline() (best for large files)
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())      #print adds newline by default, so strip away.
print()

