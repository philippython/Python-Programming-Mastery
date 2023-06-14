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
# print(square_1.area())




















        

























