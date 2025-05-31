from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.__sound = sound 

    @abstractmethod
    def make_sound(self):
        pass

    def get_sound(self):
        return self.__sound

    def __str__(self):
        return f"{self.name}_the_animal"


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} говорит: {self.get_sound()}"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} говорит: {self.get_sound()}"


if __name__ == "__main__":
    dog = Dog(name="Бобик", age=3, sound="Гав-гав")
    cat = Cat(name="Мурка", age=2, sound="Мяу")

    print(dog)  
    print(dog.make_sound())  

    print(cat)  
    print(cat.make_sound())  