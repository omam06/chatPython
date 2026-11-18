class BankingError(Exception):
    pass

class InvalidAccountError(BankingError):
    pass

class InsufficientFundsError(BankingError):
    pass


import os
import json
import random

filename = "accounts.json"
def load_accounts():
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                json_data = json.load(file)
                if isinstance(json_data, dict):
                    return json_data
                else:
                    print("❌Error: Invalid file found")
                    return {}
        except json.JSONDecodeError as e:
            print("❌Failed to load file:", e)
            return {}
    else:
        return {}

def save_accounts(accounts):
        try:
            with open(filename, "w") as file:
                json.dump(accounts, file)
                return True
        except Exception as err:
            print("❌Failed to save account:", err)
            return False
            
accounts = load_accounts()

def create_account():
    customer_name = input("Enter your name: ").strip().title()
    while not customer_name:
            print("Name must NOT be empty")
            customer_name = input("Enter your name: ").strip().title()

    while True:
        try:
            customer_age = int(input("Enter your age: "))
            if customer_age < 18:
                print("You must be atleast 18")
            else:
                break
        except ValueError:
            print("Enter a valid whole number")
    
    
    account_number = str(random.randint(1000000000, 9999999999))
    while account_number in accounts:
        account_number = str(random.randint(1000000000, 9999999999))
        
    accounts[account_number] = {
        "name": customer_name,
        "age": customer_age,
        "balance": 0,
        "transactions": []
    }    
    save_success = save_accounts(accounts)
    if save_success:
        print("Account created & saved successfully✅")
        print("Your account number is:", account_number)
    else:
        accounts.pop(account_number)
        
    
        


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
