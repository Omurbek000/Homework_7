# 1. Lists (Тизме) менен практика
# 1️⃣ fruits деген тизмени түзүп, алма, банан, өрүк, шабдалы кошуп, аны экранга чыгар.
# 2️⃣ Тизмеге "киви" жана "карбыз" кошуп, экранга чыгар.
# 3️⃣ Биринчи жана акыркы элементти тизмеден алып, экранга чыгар.

print("LIST")
fruits = ["алма", "банан", "өрүк", "шабдалы"]
print("Тizme:", fruits)
fruits.append("киви")
fruits.append("карбыз")
print("Koshkondo:", fruits)
fruits.remove(fruits[0])
print("Alganda:", fruits)
fruits.remove(fruits[-1])
print("Alganda:", fruits)


# 2. Tuples (Тупл) менен практика
# 1️⃣ colors деген тупл түзүп, ичине кызыл, көк, жашыл, сары кош.
# 2️⃣ Туплдун узундугун экранга чыгар.(count() деген методду колдонгону аракет кылып корун)
# 3️⃣ Экинчи жана акыркы элементти экранга чыгар.


print("TUPLE")
colors = ("кызыл", "кок", "жашыл", "сары")
print("TUPL:", colors)
print("Uzunlugu:", len(colors))
print("sany:", colors.count("кызыл"))
print("Ekincisi:", colors[1])
print("Akyrky:", colors[-1])


# 3. Dictionaries (Сөздүк) менен практика
# 1️⃣ student деген сөздүк түзүп, ичине  маалыматтарды сакта
# 2️⃣ Жашын 21 кылып өзгөрт жана экранга чыгар.
# 3️⃣ "группасы" деген жаңы ачкыч кошуп, ага "CS-23" маанисин бер.

print("DICTIONARY")
student = {"name": "John", "age": 20, "major": "Computer Science"}
print("Student:", student)
student["age"] = 21
print("Ozgordu:", student)
student["group"] = "CS-23"
print("Koshuldu:", student)


# 4. Sets (Жыйнак) менен практика
# 1️⃣ numbers деген жыйнак түзүп, ичине 1ден 5ке чейин сандарды кош.
# 2️⃣ 3 санын жыйнактан алып сал.

print("SET")
numbers = {1, 2, 3, 4, 5}
print("Jynak:", numbers)
numbers.remove(3)
print("Alyndy:", numbers)


# Кошумча тапшырма зээриккендерге
# List - > extend(), sort(), insert()
# Dictionary -> clear(), copy(), get(), keys(), values(), update()
# деген методдорду колдонуп коруу

print("LIST")
fruits = ["алма", "банан", "өрүк", "шабдалы"]
print("Тizme:", fruits)
fruits.extend(["киви", "карбыз"])
print("Koshkondo:", fruits)
fruits.sort()
print("Saralandy:", fruits)
fruits.insert(2, "анар")
print("Koshkondo:", fruits)


print("DICTIONARY")
student = {"name": "John", "age": 20, "major": "Computer Science"}
print("Student:", student)
student.clear()
print("Tizme:", student)
student = {"name": "John", "age": 20, "major": "Computer Science"}
print("Student:", student)
student_copy = student.copy()
print("Copy:", student_copy)
print("Student:", student)
print("Name:", student.get("name"))
print("Age:", student.get("age"))
print("Major:", student.get("major"))
print("Keys:", student.keys())
print("Values:", student.values())
student.update({"group": "CS-23"})
print("Koshuldu:", student)
print("Tizme:", student)
print("clear:", student.clear())
print("Tizme:", student)
