class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc
    def debit(self, amount):
        if amount > self.balance:
            raise ValueError("Debit amount exceeded balance")
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}")
    def credit(self, amount):
        if amount < 0:
            raise ValueError("Credit amount must be positive")
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")
    def get_balance(self):
        return self.balance
acc1 = Account(1000, "123456789")
acc1.debit(200)
acc1.credit(500)
print(f"Final balance: {acc1.get_balance()}")
print(f"Final balance: {acc1.balance}")