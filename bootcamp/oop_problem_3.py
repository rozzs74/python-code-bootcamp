# Description: Program that returns bank account information like balance, account info. Also it can deposit or withdraw money in which base
# in to available balance
# Author: John Royce Punay
# Date created: March 10, 2018 7:58 PM

class Account():

    def __init__(self, account_owner, account_balance):
        self.account_owner = account_owner
        self.account_balance = account_balance
    
    def __str__(self):
        return f"Account owner: {self.account_owner}\nAccount balance: ${self.account_balance}" 

    def withdraw_money(self, withdraw_money):
        if withdraw_money > self.account_balance:
            return "Fund Unavailable!"
        else:
            self.account_balance = self.account_balance - withdraw_money
            print(f"Current balance is {self.account_balance}")
            return "Withdrawal Accepted!"

    def deposit_money(self, deposit_money):
        self.account_balance = self.account_balance + deposit_money
        print(f"Your total balance is {self.account_balance}")
        return "Deposit Accepted"

account1 = Account("Royce", 100)
print(account1)
print(account1.deposit_money(100))
print(account1.withdraw_money(50))