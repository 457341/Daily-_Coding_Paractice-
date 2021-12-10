 #? Question 1:
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage =mileage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

#? Question 2: Create a Vehicle1 class without any variables and methods
class Vehicle1:
    pass
#? Question 3:  Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Bus(Vehicle):
#     pass
# b = Bus(100,75)
# print(b.max_speed, b.mileage)
#? Question 4: Create a Bus class that inherits from the Vehicle class. 
# ?Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Bus1(Vehicle):
    def seating_capacity(self,capacity = 50):
        Bus1.seating_capacity(self,capacity=50)
b2 = Bus1("School volvo",180,12)
print(b2.seating_capacity())

