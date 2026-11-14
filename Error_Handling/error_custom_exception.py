class InsufficientFundsError(Exception):
    pass 

def testing(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds!")
try:
    testing(500, 700)
except InsufficientFundsError as e:
    print(e)