'''ATM WIthdrawal System
Scenario
You're sinulating an ATM machine, A user inputs the amount they want to withdraw.
Task:
Raise an error if the amount is more than the account balance.Also handle non-integer input gracefully.'''
class InsufficientFundsError(Exception): pass
balance=10000
try:
    amount=int(input("Enter amount to withdraw : "))
    if amount<=0:
        raise ValueError("Withdrawl amount must be greater than 0")
    if amount>balance:
        raise InsufficientFundsError("Insufficient balance")
    balance-=amount
    print(f"Withdrawl successful! Remaining balance {balance}")
except ValueError as ve:
    print("Invalid input : ",ve)
except InsufficientFundsError as ie:
    print("Transaction failed :",ie)