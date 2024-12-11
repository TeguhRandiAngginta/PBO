class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

# Membuat objek BankAccount
account = BankAccount("John")
account.deposit(1000)
account.withdraw(500)
print(f"Remaining Balance: {account.balance}")