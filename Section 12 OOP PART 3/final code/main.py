
# class BankAccount:
#     def __init__(self, account_no, balance, password) -> None:
#         self.bank_name = "PhilipBank" # public attribute/property
#         self._account_no = account_no # protected attribute
#         self._balance = balance     
#         self.__password =  password

#     def __withdraw(self, amount):
#         self._balance -= amount

#     def deposit(self, amount):
#         self._balance += amount

#     def check_balance(self):
#         print(f"Account balance for {self._account_no} is {self._balance}")


# philip_account = BankAccount("122657888989", 900, "philip2004")
# philip_account.withdraw(200)
# philip_account.check_balance()


# print(philip_account._balance)
# print(philip_account._BankAccount__password)

# mangling __password --> _BankAccount__password

# class Car:

#     def __init__(self, max_speed, model):
#         self._max_speed = max_speed
#         self._model = model

#     # getter method -> accessor 
#     def get_max_speed(self):
#         return self._max_speed
    
#     # setter method -> mutator
#     def set_max_speed(self, new_speed):
#         if new_speed > 100:
#             print("Car speed cannnot be above 100km/h")
#         else:
#             self._max_speed = new_speed

#     def description(self):
#         print(f"Car is model {self._model} and its maximum speed is {self.get_max_speed()}")


# car = Car(70, "MD3700")
# car.set_max_speed(99)
# car.description()
    

