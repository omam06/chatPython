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
        'create a a file'
    elif operation == 2:
        'write to a file'
    elif operation == 3:
        'read to a file'
    elif operation == 4:
        'append'
    elif operation == 5:
        'rename'
    elif operation == 6:
        'delete a file'
    elif operation == 7:
        'create a dir.'
    elif operation == 8:
        'list dir. content'
    elif operation == 9:
        'explore dir. trees'
    elif operation == 10:
        print("Goodbye!")
    else:
        print("Invalid option. Must be bewteen 1 to 10")