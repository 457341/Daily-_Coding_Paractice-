

# Question:
    # Define a class, which have a class parameter and have a same instance parameter.
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name 

manzoor = Person("Manzoor")
print("%s name is %s" % (Person.name, manzoor.name))

ali = Person()
ali.name = "Ali"
print ("%s name is %s" % (Person.name, ali.name))
