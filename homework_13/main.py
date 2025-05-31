from bank_account import BankAccount
from exceptions import InsufficientFundsError, NegativeAmountError

def main():
    print("Банк эсебине кош келиңиз!")
    account = BankAccount(owner="Omurbek", balance=1000)

    while True:
        print("\nТандоо жасаңыз:")
        print("1. Баланс көрүү")
        print("2. Акча салуу")
        print("3. Акча алуу")
        print("4. Чыгуу")

        choice = input("Тандооңуз: ")

        if choice == "1":
            account.show_balance()
        elif choice == "2":
            try:
                amount = float(input("Салынуучу сумма: "))
                account.deposit(amount)
            except NegativeAmountError as e:
                print(f"Ката: {e}")
        elif choice == "3":
            try:
                amount = float(input("Алуу суммасы: "))
                account.withdraw(amount)
            except (NegativeAmountError, InsufficientFundsError) as e:
                print(f"Ката: {e}")
        elif choice == "4":
            print("Программа аяктады. Кош келиңиз!")
            break
        else:
            print("Туура эмес тандоо. Кайрадан аракет кылыңыз.")

if __name__ == "__main__":
    main()