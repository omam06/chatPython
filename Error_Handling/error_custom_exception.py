class InsufficientFundsError(Exception):
    pass 

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds!")
    elif amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    return balance - amount
try:
    new_balance = withdraw(500, 700)
except InsufficientFundsError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("New balance:", new_balance)


