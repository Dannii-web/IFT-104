from account import Account

class CurrentAccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def deposit(self,amount):
            super().deposit(amount)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds")
        super().withdraw(amount)

#user = CurrentAccount(50000)
#user.withdraw(1000)
#user.deposit(5000)



            



    