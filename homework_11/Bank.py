class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Вы успешно пополнили счёт на ${amount}."
        return "Сумма пополнения должна быть больше нуля."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Вы успешно сняли ${amount}."
        return "Недостаточно средств или некорректная сумма."

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Bank account balance: ${self.__balance}"


if __name__ == "__main__":
    account = BankAccount(100)
    print(account)

    print(account.deposit(50))
    print(account)

    print(account.withdraw(30))
    print(account)

    print(account.withdraw(150))
    print(account)

    print(f"Текущий баланс: ${account.get_balance()}")
