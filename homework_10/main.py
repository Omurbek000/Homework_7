class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"'{self.title}' деген китепти {self.author} {self.year}-жылы жазган"

    def is_classic(self):
        return self.year < 1970

book = Book("Абай жолу", "Мухтар Ауэзов", 1942)
print(book.get_summary())  
print(book.is_classic())  


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def is_electric(self):
        return self.make.lower() == "tesla"


car = Car("Tesla", "Model S", 2022)


print(car.get_description())  
print(car.is_electric())      