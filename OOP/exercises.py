 #? Question 1:
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage =mileage

#? Question 2: Create a Vehicle1 class without any variables and methods
class Vehicle1:
    pass
#? Question 3:  Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass
b = Bus(100,75)
print(b.max_speed, b.mileage)