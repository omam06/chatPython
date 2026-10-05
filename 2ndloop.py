books = ['Python Crash Course', 'Atomic Habits', 'Deep Work']
option = 0
while option != 5:

    print("===== USER PROFILE =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    option = int(input("Choose your option (1, 2, 3, 4, 5): "))

    if option == 1:
        for book in books:
            print(book)

    elif option == 2:
        add = input("book name: ")
        books.append(add)
        print("Book added successfully!")

    elif option == 3:
        search = input("book name: ")
        if search in books:
            print("Book Found")
        else:
            print("Not found!")

    elif option == 4:
        remover = input("book name: ")
        gone = books.remove(remover)
        print("Book removed successfully")

    elif option == 5:
        print("Goodbye!")
    
    