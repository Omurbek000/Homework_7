# 1. Колдонуучудан пин код сура
# Эгер туура эмес болсо, 3 жолу туура эмес болсо программа токтот
# 2. Пин код туура болсо, төмөнкү менюну көрсөт
# 3. Ар бир операцияда:
#    - Акчаны текшергенде балансты көрсөт
#    - Акча алганда:
#      - Колдонуучудан сумма сура
#      - Эгер каражат жетишсиз болсо, raise менен ката ыргытып аны except менен карма
#    - Акча салганда сумма кош
#      - Терс сумма болсо ката ыргытып токтот

balance = 1000
pin_code = "1234"
attempts = 0

while attempts < 3:
    entered_pin = input("🔑 Пин кодду киргизиңиз: ")
    if entered_pin == pin_code:
        print("\n✅ Пин код туура!")
        while True:
            try:
                print("\n📋 Меню:")
                print("1️⃣  Балансты текшерүү")
                print("2️⃣  Акча алуу")
                print("3️⃣  Акча салуу")
                print("4️⃣  Чыгуу")
                choice = input("👉 Тандоо жасаңыз: ")

                if choice == "1":
                    print(f"\n💰 Учурдагы баланс: {balance} сом")
                elif choice == "2":
                    amount = int(input("\n💵 Сумманы киргизиңиз: "))
                    if amount > balance:
                        raise ValueError("❌ Каражат жетишсиз!")
                    balance -= amount
                    print(f"\n✅ {amount} сом алынды. Жаңы баланс: {balance} сом")
                elif choice == "3":
                    amount = int(input("\n💵 Сумманы киргизиңиз: "))
                    if amount <= 0:
                        raise ValueError("❌ Терс же нөл сумма киргизүүгө болбойт!")
                    balance += amount
                    print(f"\n✅ {amount} сом кошулду. Жаңы баланс: {balance} сом")
                elif choice == "4":
                    print("\n👋 Программа жабылууда...")
                    break
                else:
                    print("\n❌ Туура эмес тандоо!")
            except ValueError as e:
                print(f"\n⚠️ Ката: {e}")
            finally:
                print("\n🙏 Келгениз үчүн рахмат!")
        break
    else:
        attempts += 1
        print(f"\n❌ Пин код туура эмес! Калган мүмкүнчүлүк: {3 - attempts}")
else:
    print("\n🚫 3 жолу туура эмес пин код киргизилди. Программа токтотулду.")



