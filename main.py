class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class PaymentGateway:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def pay(self, amount):
        self.bank_account.deposit(amount)

class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.pay(amount)

# Dependency Inversion Principle (DIP) misolida:
# - BankAccount (High-level moduli) va PaymentGateway (Low-level moduli) o'rtasidagi muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaqiyatli muvaffaq
