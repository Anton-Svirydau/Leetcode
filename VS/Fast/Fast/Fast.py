from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!

'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "No amount"

    def get_balance(self):
        return self.__balance 

account = BankAccount(1000)
print(account.get_balance())  # 1000
# print(account.__balance)  # Error: AttributeError
'''

'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Driving"

class Car(Vehicle):
    def drive(self):
        return f"{self.brand} is driving fast"

car = Car("Toyota")
print(car.drive())  # Toyota is driving fast
'''

'''
class Bird:
    def make_sound(self):
        return "Chirp!"

class Duck(Bird):
    def make_sound(self):
        return "Quack!"

def animal_sound(animal):
    return animal.make_sound()  # Work with any object, that have make_sound()

bird = Bird()
duck = Duck()
print(animal_sound(bird))  # Chirp!
print(animal_sound(duck))  # Quack!
'''

