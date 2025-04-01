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


