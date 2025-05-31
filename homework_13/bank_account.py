from exceptions import InsufficientFundsError, NegativeAmountError

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Сиз терс сумма сала албайсыз.")
        self.balance += amount
        print(f"{amount} сом кошулду. Жаңы баланс: {self.balance} сом.")

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Сиз терс сумма ала албайсыз.")
        if amount > self.balance:
            raise InsufficientFundsError("Акча жетишсиз.")
        self.balance -= amount
        print(f"{amount} сом алынды. Жаңы баланс: {self.balance} сом.")

    def show_balance(self):
        print(f"Учурдагы баланс: {self.balance} сом.")