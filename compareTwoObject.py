# Write a Python program to add two objects if both objects are an integer type.
def add_objects(obj1,obj2):
    if (type(obj1) and type(obj2)) == int:
        return obj1 + obj2
    


print(type(10))
print(add_objects(2,3))