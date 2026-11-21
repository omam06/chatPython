class BankingError(Exception):
    pass

class InvalidAccountError(BankingError):
    pass

class InsufficientFundsError(BankingError):
    pass


import os
import json
import random
from decimal import Decimal, InvalidOperation

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
        print("Account creation failed. Please try again")


def check_balance():
    acct_num = input("Enter account number: ").strip()
    if acct_num in accounts:
        account = accounts[acct_num]
        print(f"Account Balance for {account['name']} is ₦{account['balance']}")
    else:
        raise InvalidAccountError("Oooppss❗ Account does NOT exist")
    
def deposit():
    acct_num = input("Enter account number: ").strip()
    if acct_num not in accounts:
        raise InvalidAccountError("Account does NOT exist❌")

    while True:
        amount = input("Enter deposit amount: ").strip()
        try:
            dep_amount = Decimal(amount)
        except InvalidOperation:
            print("Invalid input. Amount MUST be a valid number")
            continue
        if dep_amount <= 0:
            print("Deposit amount MUST be more than 0")
            continue
        deposit_amount = dep_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        
        if deposit_amount <= 0:
            print("Deposit amount rejected🚫 MUST be greater than zero")
            continue
        
        account = accounts[acct_num]
        initial_balance = account["balance"]
        account["balance"] += deposit_amount

        save_success = save_accounts(accounts)
        if save_success:
            print(f"Deposit of ₦{deposit_amount} successful✅")
            print(f"New balance: ₦{account['balance']}")
            break
        else:
            account["balance"] = initial_balance
            print(f"Deposit failed❌ Balance: {initial_balance}")
            continue


while True:
    print("\n========== PERSONAL BANKING SYSTEM ==========")

    print("1. Create account")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. View transaction history")
    print("7. Exit")

    operation = input("Choose an operation: ").strip()

    if operation == "1":
        create_account()
    elif operation == "2":
        try:
            check_balance()
        except InvalidAccountError as err:
            print(err)
    elif operation == "3":
        pass
    elif operation == "4":
        pass
    elif operation == "5":
        pass
    elif operation == "6":
        pass
    elif operation == "7":
        print("Bye!👋 See you again")
        break
    else:
        print("Invalid option. Must be from 1-7")
