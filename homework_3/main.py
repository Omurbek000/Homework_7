# Алгач ар бир маалыматты өзүнчө өзгөрмө (variable) катары сактайбыз
# Андан кийин, баарын бир dictionary'ге (сөздүк — ачкыч-маани менен сактоочу структура) салабыз
# Акырында — ошол маалыматтардан креативдүү паспорт баракча чыгарабыз 🎨📘

variable = 'pasport'

dictionary = {
    'surname': 'Иванов',
    'name': 'Иван',
    'patronymic': 'Иванович',
    'birth_date': '01.01.2000',
    'birth_place': 'Москва',
    'passport_number': '1234 567890',
    'issue_date': '01.01.2020',
    'expiry_date': '01.01.2030',
    'issued_by': 'УВД г. Москвы',
}


print('=====================================')
print('🎨📘 ПАСПОРТ МААЛЫМАТТАРЫ 📘🎨')
print('=====================================')
print(f'🆔 Фамилия:       {dictionary["surname"]}')
print(f'🆔 Имя:           {dictionary["name"]}')
print(f'🆔 Отчество:      {dictionary["patronymic"]}')
print(f'🎂 Дата рождения: {dictionary["birth_date"]}')
print(f'📍 Место рождения: {dictionary["birth_place"]}')
print(f'📄 Номер паспорта: {dictionary["passport_number"]}')
print(f'📅 Дата выдачи:   {dictionary["issue_date"]}')
print(f'📅 Дата окончания: {dictionary["expiry_date"]}')
print(f'🏢 Выдан:         {dictionary["issued_by"]}')
print('=====================================')
print('💟')
