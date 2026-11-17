while True:
    print("========== PERSONAL BANKING SYSTEM ==========")

    print("1. Create account")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. View transaction history")
    print("7. Exit")

    operation = input("Choose an operation: ").strip()

    if operation == "1":
        # create acc
    elif operation == "2":
        #check bal
    elif operation == "3":
        #deposit
    elif operation == "4":
        #withdraw
    elif operation == "5":
        #transfer
    elif operation == "6":
        #history
    elif operation == "7":
        break
    else:
        print("Invalid option. Must be from 1-7")
