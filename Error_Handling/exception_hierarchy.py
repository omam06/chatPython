# Assuming our banking app has several custom errors we gotta catch, Instead of making each one inherit directly from Exception, we can create our own parent exception.

class BankingError(Exception):
    pass

class InsufficientFundsError(BankingError):
    pass

class InvalidAccountError(BankingError):
    pass

class AccountFrozenError(BankingError):
    pass 

try:
    raise AccountFrozenError("This account is frozen!")

except InsufficientFundsError as e:
    print("Insufficient funds:", e)

except BankingError as e:                                        # this will handle acctfrozen cos its the parent class
    print("Banking problem:", e)