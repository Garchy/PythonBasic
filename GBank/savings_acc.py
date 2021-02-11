from account import Account

class Savings_Account(Account):
    def withdraw(self, amount):
        if self._balance < amount:
            print("Insufficient Funds")
            return
        
        self._balance -= amount
        self.details()

    def deposit(self, amount):
        self._balance += amount 
        self.details()
    