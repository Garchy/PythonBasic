class Bank:
    def __init__(self):
        self.agencys = [1111, 2222, 3333]
        self.clients = []
        self.accounts = []

    def add_clients(self, client):
        self.clients.append(client)

    def add_accounts(self, account):
        self.accounts.append(account)

    def validate(self, client):
        if client not in self.clients:
            return None

        if client.account not in self.accounts:
            return False
        
        if client.account.agency not in self.agencys:
            return False
        
        return True