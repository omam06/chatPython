import os 

def create_file():
    filename = input("Enter filename: ").strip()
    if not filename:
        print("Filename cannot be empty!")
    elif os.path.isfile(filename):
        print(f"A file called {filename} already exists")
    elif os.path.exists(filename):
        print(f"A directory with the name {filename} already exists")
    elif os.path.exists(filename):
        print(f"An entry with the name {filename} already exists")
    else:
        try:
            with open(filename, "w") as file:
                pass
            print(f"{filename} created successfully!")
        except OSError as err:                   #OS may reject filename cos of symbols, filesystem-related errors - FileNotFoundError, PermissionError, and IsADirectoryError
            print(f"Failed to create file: {err}")

def write_to_file():
    filename = input("Enter the name of file to which you wish to write: ").strip()
    if not filename:
        print("Filename must not be empty")
    elif not os.path.exists(filename):
        print("❌File not found")
    elif not os.path.isfile(filename):
        print("Matching document is not a file.")
    else:
        text = input("Enter content: ")
        try:
            with open(filename, "w") as file:
                file.write(text)
            print("Writing to file successful ✅")  
        except OSError as err:
            print(f"❌Failed to write to file: {err}")

def read_file():
    filename = input("Enter the file name: ").strip()
    if not filename:
        print("Filename must not be empty")
    elif not os.path.exists(filename):
        print("❌ File does not exist")
    elif not os.path.isfile(filename):
        print("Matching document is not a file.")
    else:
        try:
            with open(filename, "r") as file:
                content = file.read()
                if not content:
                    print("File is empty")
                else:
                    print(content)
        except OSError as er:
            print(f"❌ Failed to read file: {er}")


def append_to_file():
    filename = input("Enter file name: ").strip()
    if not filename:
        print("Filename must not be empty")
    elif not os.path.exists(filename):
        print("❌ File does not exist")
    elif not os.path.isfile(filename):
        print("Matching document is not a file.")
    else:
        try:
            text = input("Enter text: ")
            size = os.path.getsize(filename)
            if size == 0:
                content = text
            else:
                with open(filename, "r") as file:
                    old_content = file.read()
                if old_content[-1] == "\n":
                    content = text 
                else:
                    content = f"\n{text}"
            
            with open(filename, "a") as file:
                file.write(content)
            print(f"Appending text to {filename} successful ✅")
                
        except OSError as e:
            print(f"❌ Failed to append: {e}")


def rename_a_file():
    filename = input("Enter filename: ").strip()
    if not filename:
        print("Filename must not be empty")
    elif not os.path.exists(filename):
        print("❌ File does not exist")
    elif not os.path.isfile(filename):
        print("Matching document is not a file.")
    else:
        new_name = input("Enter new file name: ").strip()
        if not new_name:
            print("New name must not be empty.")
        elif os.path.dirname(new_name) != "":
            print(f"{new_name} must be a file name, not another path.")
        else:
            directory = os.path.dirname(filename)
            new_path = os.path.join(directory, new_name)
            if os.path.exists(new_path):
                print("That already exists.")
            else:
                try:
                    os.rename(filename, new_path)
                    print(f"File renamed to {new_path} successfully ✅")
                except OSError as e:
                    print(f"❌ Failed to rename file: {e}")

def delete_a_file():
    filename = input("Enter file name: ").strip()
    if not filename:
        print("Filename must not be empty!")
    elif not os.path.exists(filename):
        print("❌ File does not exist")
    elif not os.path.isfile(filename):
        print("Matching document is not a file.")
    else:
        try:
            os.remove(filename)
            print(f"{filename} deleted successfully ✅")
        except OSError as error:
            print(f"❌ Failed to delete file: {error}")


def create_directory():
    new_directory = input("Enter directory path: ").strip()
    if not new_directory:
        print("Directory path must not be empty!")
    elif os.path.exists(new_directory):
        print("Oooppsss 😬 Directory already exists")
    elif os.path.isfile(new_directory):
        print("Matching result is a file, not a directory.")
    else:
        ask = input("Is this a single or a nested directory? (Single/Nested): ").strip().title()
        while ask not in ["Single", "Nested"]:
            print("Invalid answer.")
            ask = input("Is this a single or a nested directory? (Single/Nested): ").strip().title()
        try:
            if ask == "Single":
                os.mkdir(new_directory)
            elif ask == "Nested":
                os.makedirs(new_directory)
        except OSError as e:
            print(f"❌ Failed to create directory: {e}")
        else:
            print(f"{new_directory} created successfully ✅")

def list_directory_contents():
    directory = input("Enter directory path: ").strip()
    if not directory:
        print("Directory path must not be empty")
    elif not os.path.exists(directory):
        print("Directory not found ❌")
    elif not os.path.isdir(directory):
        print("Matching result is not a directory")
    else:
        try:
            content = os.listdir(directory)
            if not content:
                print(f"Nothing to see here in {directory}")
            else:
                print(content)
        except OSError as e:
            print(f"❌ Failed to list directory contents: {e}")

def explore_directory():
    directory = input("Enter directory path: ").strip()
    if not directory:
        print("Directory path must not be empty!")
    elif not os.path.exists(directory):
        print(f"{directory} not found ❌")
    elif not os.path.isdir(directory):
        print("Matching result is not a directory")
    else:
        try:
            for root, dirs, files in os.walk(directory):
                print(f"Directory: {root}")
                print(f"Subdirectories: {dirs}")
                print(f"Files: {files}")

        except OSError as err:
            print(f"Failed to explore {directory}: {err}")


operation = 1
while operation != 10:
    print("\n========== PERSONAL FILE MANAGER ==========")
    print("1. Create a file")
    print("2. Write to a file")
    print("3. Read a file")
    print("4. Append to a file")
    print("5. Rename a file")
    print("6. Delete a file")
    print("7. Create a directory")
    print("8. List directory contents")
    print("9. Explore directory tree")
    print("10. Exit")

    valid_input = False
    while not valid_input:
        try:
            operation = int(input("Choose an operation: "))
            valid_input = True
        except ValueError:
            print("Invalid input. Enter valid integer(s)")
    
    if operation == 1:
        create_file()
    elif operation == 2:
        write_to_file()
    elif operation == 3:
        read_file()
    elif operation == 4:
        append_to_file()
    elif operation == 5:
        rename_a_file()
    elif operation == 6:
        delete_a_file()
    elif operation == 7:
        create_directory()
    elif operation == 8:
        list_directory_contents()
    elif operation == 9:
        explore_directory()
    elif operation == 10:
        print("Goodbye!")
    else:
        print("Invalid option. Must be between 1 to 10")
