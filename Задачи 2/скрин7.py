class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        commission = amount * 0.01
        total_amount = amount - commission
        self.balance += total_amount
        print(f"Депозит {total_amount} успешно проведен. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        else:
            commission = amount * 0.01
            total_amount = amount + commission
            self.balance -= total_amount
            print(f"Снятие {total_amount} успешно проведено. Новый баланс: {self.balance}")

    def check_balance(self):
        print(f"Баланс на счете {self.account_number} составляет: {self.balance}")

# пример использования
account1 = BankAccount("123456", "Иванов Иван", 1000)
account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

account2 = BankAccount("654321", "Петров Петр", 2000)
account2.check_balance()
account2.withdraw(500)
account2.deposit(1000)
account2.check_balance()
