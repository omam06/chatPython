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
print()

#os.path.join() - combines path components into one valid path.
path_ = os.path.join("Study_Projects", "lupject.py")
print(path_)                           #---> Study_Projects/lupject.py
print()

#os.path.basename() -  Extracts the final component of a path (usually the filename).
path_ = "Study_Projects/lupject.py"

print(os.path.basename(path_))              #---> lupject.py
print(os.path.dirname(path_))                 # Extracts the directory part of a path --> Study_Projects
print()

# os.path.abspath()  -  Converts a path into an absolute path.
print(os.path.abspath("my_notes.txt"))

# .path.splitext()  -  Separates a path into its name and extension(.py) in a tuple.
print(os.path.splitext(path_))                   # receive only filename as parameter too

print(os.path.getsize("my_notes.txt"))                      #Return the size of a file in bytes.
print()

# os.path.isabs()  -  Checks whether a path is absolute.
print(os.path.isabs("my_notes.txt"))
print(os.path.isabs("/home/student/chatPython/my_notes.txt"))


"""Function	Purpose
os.mkdir()	Creates a directory
os.makedirs()	Creates directories, including nested ones
os.rmdir()	Removes an empty directory
os.remove()	Deletes a file
os.rename()	Renames or moves a file or directory
	
os.walk()	Traverses directories and their subdirectories"""

folder = "Study_Projects"
subfolder = "exercises"
filename = "loops.py"

print(os.path.join(folder, subfolder, filename))
print()

# os.scandir()  -  unlike os.listdir(), which gives us just the names of directory contents, os.scandir() gives us directory entries that provide additional information. It lets us inspect individual entries to determine whether they're files or directories
with os.scandir("Study_Projects") as entries:
    for entry in entries:
        print()
        print(entry.name)
        print(entry.is_file())
        print(entry.is_dir())
        if entry.is_file():
            print(entry.name, "is a file")
        elif entry.is_dir():
            print(entry.name, "is a directory")
print()

# os.mkdir("New_Folder") creates 1 directory inside cwd
# os.makedirs - create 1 dir with nested dirs inside(no file). it expect a path as it's 1st argument nested dir: os.makedirs("Projects/Python/File_Handling")

"""import os

folders = ["Python", "Projects", "Exercises"]

subfolders = ["Folder1", "Folder2", "Folder3", "Folder4", "Folder5"]

for folder in folders:
    for subfolder in subfolders:
        path = os.path.join(folder, subfolder)
        os.mkdir(path)
Python/Folder1
Python/Folder2
Python/Folder3
Python/Folder4
Python/Folder5 etc """

# os.remove("notes.txt")  -  deletes a file, not directory.
# os.rmdir("Python")  -  removes an empty directory. Rraises an OSError if the directory contains files or other directories
# shutil.rmtree("Study_Projects")  -  deletes non-empty directory. shell utilities is a python module you import (shutil) 
""" Renaming and moving files/directories
os.rename("my_notes.txt", "python_notes.txt")               file is renamed
os.rename("python_notes.txt", "Projects/python_notes.txt")        file is moved inside Projects dir. w same name, can rename while moving too.
os.rename("Projects", "My_Projects")                           rename directories too

shutil.move("old_notes.txt", "Projects/")                       file is moved inside projects dir. shutil.move() 4 moving files & dir."""

# os.walk() -  exploring an entire directory and all its nested directories automatically
for root, dirs, files in os.walk("."):             #automatically visits nested directories. You don't have to write nested loops to descend into them.
    print(root)
    print(dirs)
    print(files)
print()

# To print the full paths of every file inside a directory and all its subdirectories
for root, dirs, files in os.walk("."):
    for filename in files:
        file_path = os.path.join(root, filename)
        print(file_path)                    #--> ./Study_Projects/dict_project.py