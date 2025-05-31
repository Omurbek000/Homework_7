class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        return f"Я студент. Меня зовут {self.name}, мне {self.age} лет, мой класс: {self.grade}."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Я учитель. Меня зовут {self.name}, мне {self.age} лет, я преподаю: {self.subject}."


if __name__ == "__main__":
    person = Person("Омурбек", 30)
    student = Student("Омурбек", 30, "10A")
    teacher = Teacher("Омурбек", 30, "Математика")

    print(person.introduce())
    print(student.introduce())
    print(teacher.introduce())


