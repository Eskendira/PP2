"""Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass"""

class Account():
    def __init__(self, owner:str, balance = 0):
        self.owner = owner
        self.balance = balance
    def dep(self, add):
        self.add = add
        self.balance = self.balance + add
    def withdr(self, withdraw):
        self.withdraw = withdraw
        if(self.balance - withdraw >= 0):
            self.balance = self.balance - withdraw
            print("money withdrawn")
            print('осталось на карте: ' + str(self.balance))
        else:
            print('not enough money')
    def info(self):
        print('name: ' + self.owner)
        print('balance: ' + str(self.balance))

p = Account('Nuray', 300)
p.dep(200)
p.withdr(600)
p.info()     