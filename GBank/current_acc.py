from account import Account

class Current_Account(Account):
    def __init__(self, agency, account_number, balance, limit = 100):
        super().__init__(agency, account_number, balance)
        self._limit = limit
    
    @property
    def limit(self):
        return self._limit

    def withdraw(self, amount):
        if (self.balance + self.limit) < amount:
            print("Insufficient Funds")
            return

        self._balance -= amount
        self.details()

    def deposit(self, amount):
        self._balance += amount 
        self.details()
