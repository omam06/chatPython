books = ['Python Crash Course', 'Atomic Habits', 'Deep Work']
option = 0
while option != 5:
    
    print("====== USER PROFILE ======")
    print("1. View Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    option = int(input("Choose an option (1, 2, 3, 4, 5): "))

    if option == 1:
# To View Books
        for book in books:
            print(book)

    elif option == 2:
# To Add Book
        newbook = input("Enter book name: ")
        books.append(newbook)
        print("Book added successfully!")

    elif option == 3:
# To Search book
        search = input("Enter book name: ")
        found = "Book not found."
        for book in books:
            if search == book:
                found = "Book found!"
                break
        print(found)
                

    elif option == 4:
# To remove book
        discard_book = input("Enter book name: ")
        if discard_book in books:
            books.remove(discard_book)
            print("Book removed!")
        else:
            print("Book not found!")

    elif option == 5:
# Exit the Program
        print("Goodbye!")

