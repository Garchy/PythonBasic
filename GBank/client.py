from person import Person
from savings_acc import Savings_Account
from current_acc import Current_Account

class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None

    def create_account(self, account):
        self.account = account