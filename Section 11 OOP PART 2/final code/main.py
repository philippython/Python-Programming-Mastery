# class Animal:
    # Base class, parent class Animal

    # def breath(self):
    #     print("Animals can breath")

    # def growth(self):
    #     print("Animals can grow")


# class AquaticAnimal(Animal):
    # child class, a sub class or a derived class
#     def swim(self):
#         print("Animal can swim")

# fish = AquaticAnimal()
# fish.breath()
# fish.growth()
# fish.swim()        

# animal = Animal()
# animal.swim()


# class Vehicle:

#     def __init__(self, max_speed, color) -> None:
#         self.max_speed = max_speed
#         self.color = color

#     def accelerate(self):
#         print(f"Car is accelerating and it can't accelrate above {self.max_speed}")

# class FasterVehicle(Vehicle):

#     def __init__(self, max_speed, color):
#         super().__init__(max_speed, color)
#         self.max_speed = max_speed

#     # method overriding
#     def accelerate(self):
#         print(f"Faster Car is accelrating and it can't accelrate above {self.max_speed}")


# vehicle = Vehicle(70, "Blue")
# vehicle.accelerate()

# faster_car = FasterVehicle(80, "Red")
# faster_car.accelerate()

# class Base: 

#     depth = 1
#     def test(self):
#         print("I am the Test method in Base class")

# class Base2:

#     depth = 2
#     def test(self):
#         print("I am the Test method in Base2 class")

# class Base3(Base, Base2) : #inheritance list
    # method resolution order follows a linear order , left --> right
    # pass
    # def test(self):
    #     print("I am the Test method in Base 3")


# base_3 = Base3()
# base_3.test()
# print(base_3.depth)


# class Shape:

#     def area(self):
#         pass


# class Rectangle(Shape):

#     def __init__(self, length, breadth):
#         super().__init__()
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth
    
# class Square(Shape):

#     def __init__(self, length) -> None:
#         super().__init__()
#         self.length = length

#     def area(self):
#         return self.length ** 2
    

# rect_1 = Rectangle(2, 3)
# square_1 = Square(3)

# print(rect_1.area())
# print(square_1.area()






# Challenge: Vehicle Hierarchy

# Create a hierarchy of vehicles with the following specifications:

# The base class should be called Vehicle and should have the following attributes:

# manufacturer (string): The manufacturer of the vehicle.
# model (string): The model of the vehicle.
# year (integer): The manufacturing year of the vehicle.
# The Vehicle class should have the following methods:

# get_details(): Prints the details of the vehicle, including the manufacturer, model, and year.
# class Vehicle:

#     def __init__(self, manufacturer: str, model: str, year:int) -> None:
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
        
#     def get_details(self):
#         print(f"This vehicle was manufactured by {self.manufacturer} model {self.model} built in year {self.year}")

# Implement the following derived classes:

# a) Car class:

# Inherits from Vehicle.
# Should have an additional attribute called num_doors (integer) representing the number of doors the car has.

# class Car(Vehicle):

#     def __init__(self, manufacturer: str, model: str, year: int, num_doors: int) -> None:
#         super().__init__(manufacturer, model, year)
#         self.num_doors = num_doors

#     def get_details(self):
#         print(f"{self.manufacturer} built model {self.model} with {self.num_doors} doors in the year {self.year}")

# b) Motorcycle class:

# Inherits from Vehicle.
# Should have an additional attribute called top_speed (float) representing the maximum speed of the motorcycle.

# class MotorCycle(Vehicle):

#     def __init__(self, manufacturer: str, model: str, year: int, top_speed) -> None:
#         super().__init__(manufacturer, model, year)
#         self.top_speed = top_speed

#     def get_details(self):
#         print(f"{self.manufacturer} built model {self.model} with a top speed of {self.top_speed} in the year {self.year}")
# c) Truck class:

# Inherits from both Car and Vehicle.
# class Truck(Car):

#     def __init__(self, manufacturer: str, model: str, year: int, num_doors: int, cargo_capacity: float) -> None:
#         super().__init__(manufacturer, model, year, num_doors)
#         self.cargo_capacity = cargo_capacity

#     def get_details(self):
#         print(f"{self.manufacturer} built model {self.model} with a cargo capacity of {self.cargo_capacity} with {self.num_doors} doors in the year {self.year}")

# Should have an additional attribute called cargo_capacity (float) representing the maximum cargo capacity in tons.
# Override the get_details() method in each derived class to display the specific details of that vehicle type. For example:

# For a car, the output should include the number of doors.
# For a motorcycle, the output should include the top speed.
# For a truck, the output should include the cargo capacity.
# Your task is to implement the above class hierarchy and test it by creating instances of each class and calling their respective get_details() methods.

# volvo = Vehicle("Volvo", "PPM67959", 2007)
# volvo.get_details()

# toyota = Car("Toyota", "Corolla", 2009, 4)
# toyota.get_details()

# bajaj = MotorCycle("Bajaj", "TRYM567", 2008, 200)
# bajaj.get_details()

# truck = Truck("Mistubushi", "MTS1221", 2010, 4, 700)
# truck.get_details()





















        

























