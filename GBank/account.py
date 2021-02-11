from abc import abstractmethod, ABC

class Account(ABC):
    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    @property
    def agency(self):
        return self._agency
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def deposit(self, amount):
        self._balance += amount 
        self.details()
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def details(self):
        print()
        print(f"Agency: {self._agency}")
        print(f"Account: {self._account_number}")
        print(f"Balance: {self._balance}")
    
