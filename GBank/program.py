from bank import Bank
from client import Client
from account import Account
from current_acc import Current_Account
from savings_acc import Savings_Account

bank = Bank()

client1 = Client("Alex Green", 22)
client2 = Client("Maria Silva", 33)
client3 = Client("Bob Brown", 40)

bank.add_clients(client1)
bank.add_clients(client2)
bank.add_clients(client3)

acc1 = Savings_Account(1111, 123456, 0)
acc2 = Current_Account(2222, 987654, 0)
acc3 = Savings_Account(3333, 123987, 0)

bank.add_accounts(acc1)
bank.add_accounts(acc2)
bank.add_accounts(acc3)

client1.create_account(acc1)
client2.create_account(acc2)
client3.create_account(acc3)



if bank.validate(client1):
    client1.account.deposit(0)
    client1.account.withdraw(10)
else:
    print("\nUnverified client")

print("###########")

if bank.validate(client2):
    client2.account.deposit(0)
    client2.account.withdraw(10)
else:
    print("\nUnverified client")