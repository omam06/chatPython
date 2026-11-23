import os
import json
import random
import copy
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import datetime


class BankingError(Exception):
    pass

class InvalidAccountError(BankingError):
    pass

class InsufficientFundsError(BankingError):
    pass



filename = "accounts.json"
def load_accounts():
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                json_data = json.load(file)
                if isinstance(json_data, dict):
                    for each_acct in json_data:
                        json_data[each_acct]["balance"] = Decimal(json_data[each_acct]["balance"]) 
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
            accounts_copy = copy.deepcopy(accounts)
            for each_account in accounts_copy:
                accounts_copy[each_account]["balance"] = str(accounts_copy[each_account]["balance"])
            with open(filename, "w") as file:
                json.dump(accounts_copy, file)
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
        "balance": Decimal("0.00"),
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
    acct_num = input("Enter your account number: ").strip()
    if acct_num in accounts:
        account = accounts[acct_num]
        print(f"Account Balance for {account['name']} is ₦{account['balance']}")
    else:
        raise InvalidAccountError("Oooppss❗ Account does NOT exist")
    
def deposit():
    acct_num = input("Enter your account number: ").strip()
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
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if deposit_amount <= 0:
            print("Deposit amount rejected🚫 MUST be greater than zero")
            continue
        
        account = accounts[acct_num]
        initial_balance = account["balance"]
        account["balance"] += deposit_amount
        account["transactions"].append({
            "type": "deposit", 
            "amount": str(deposit_amount), 
            "timestamp": timestamp
        })

        save_success = save_accounts(accounts)
        if save_success:
            print(f"Deposit of ₦{deposit_amount} successful✅")
            print(f"New balance: ₦{account['balance']}")
            break
        else:
            account["balance"] = initial_balance
            print(f"Deposit failed❌ Balance: {initial_balance}")
            account["transactions"].pop()
            continue

def withdrawal():
    acct_num = input("Enter your account number: ").strip()
    if acct_num not in accounts:
        raise InvalidAccountError("Account does NOT exist❌")

    while True:
        amount = input("Enter withdrawal amount: ").strip()
        try:
            withdraw_amount = Decimal(amount)
        except InvalidOperation:
            print("Invalid input. Amount MUST be a valid number")
            continue
        if withdraw_amount <= 0:
            print("Withdrawal amount MUST be more than 0")
            continue
        
        withdrawal_amount = withdraw_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if withdrawal_amount <= 0:
            print("Withdrawal rejected🚫 Amount MUST be more than 0")
            continue

        account = accounts[acct_num]
        original_balance = account["balance"]
        if withdrawal_amount > original_balance:
            raise InsufficientFundsError("Insufficient Funds!")

        account["balance"] = original_balance - withdrawal_amount

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account["transactions"].append({
            "type": "withdrawal", 
            "amount": str(withdrawal_amount), 
            "timestamp": timestamp
        })

        

        save_success = save_accounts(accounts)
        if save_success:
            print(f"Withdrawal of ₦{withdrawal_amount} successful✅")
            print(f"Balance: ₦{account['balance']}")
            print()
            break
        else:
            account["balance"] = original_balance
            print(f"Withdrawal failed❌ Balance: {original_balance}")
            account["transactions"].pop()
            continue

def transfer():
    sender_acct = input("Enter your account number: ").strip()
    if sender_acct not in accounts:
        raise InvalidAccountError("Account does NOT exist❌")
    
    recipient_acct = input("Enter recipient account number: ").strip()
    if recipient_acct not in accounts:
        raise InvalidAccountError("Account does NOT exist❌")
    if sender_acct == recipient_acct:
        print("You canNOT transfer to same account❌")
        return
    
    while True:
        amount = input("Enter transfer amount: ").strip()
        try:
            send_amount = Decimal(amount)
        except InvalidOperation:
            print("Invalid input. Amount MUST be a valid number")
            continue
        if send_amount <= 0:
            print("Transfer amount MUST be more than 0")
            continue

        transfer_amount = send_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if transfer_amount <= 0:
            print("Transfer rejected🚫 Amount MUST be more than 0")
            continue

        sender_bal = accounts[sender_acct]["balance"]   
        if transfer_amount > sender_bal:
            raise InsufficientFundsError("Insufficient funds!")

        receiver_bal = accounts[recipient_acct]["balance"]
        
        accounts[sender_acct]["balance"] -= transfer_amount
        accounts[recipient_acct]["balance"] += transfer_amount
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        accounts[sender_acct]["transactions"].append({
            "type": "transfer_out", 
            "amount": str(transfer_amount),
            "recipient": recipient_acct, 
            "timestamp": timestamp
        })
        
        accounts[recipient_acct]["transactions"].append({
            "type": "transfer_in", 
            "amount": str(transfer_amount),
            "sender": sender_acct, 
            "timestamp": timestamp
        })
        
        save_success = save_accounts(accounts)
        if save_success:
            print(f"Withdrawal of ₦{withdrawal_amount} successful✅")
            print(f"Balance: ₦{account['balance']}")
            print()
            break
        else:
            account["balance"] = original_balance


def transaction_history():
    acct_num = input("Enter account number: ").strip()
    if acct_num not in accounts:
        raise InvalidAccountError("Account does NOT exist❌")
    
    account = accounts[acct_num]
    if not account["transactions"]:
        print("Nothing to see here! No transaction history found.")
        return

    for each_transaction in account["transactions"]:
        print(f"Transaction Type: {each_transaction['type'].title()}")
        print(f"Amount: {each_transaction['amount']}")
        print(f"Date & Time: {each_transaction['timestamp']}")
        print("_______________________________________________________________")

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
        try:
            deposit()
        except InvalidAccountError as e:
            print(e)
    elif operation == "4":
        try:
            withdrawal()
        except (InvalidAccountError, InsufficientFundsError)  as e:
            print(e)
    elif operation == "5":
        pass
    elif operation == "6":
        transaction_history()
    elif operation == "7":
        print("Bye!👋 See you again")
        break
    else:
        print("Invalid option. Must be from 1-7")
