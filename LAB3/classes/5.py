"""Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass"""

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, num):
        self.balance += num
        print(f"Deposit of {num} successful. Current balance: {self.balance}")
    def withdraw(self, num):
        if num > self.balance:
            print('Not enough money')
        else:
            self.balance -= num
            print(f"Withdrawal of {num} successful. Current balance: {self.balance}")