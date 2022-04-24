class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def withdraw(self, amt):
        self.balance -= amt
        return self.balance


if __name__ == '__main__':
    acct = BankAccount('Guru')
    print(f"account owner : {acct.owner}, account balance : {acct.balance}")
    print(acct.deposit(10))
    print(acct.withdraw(3))
    print(acct.balance)
