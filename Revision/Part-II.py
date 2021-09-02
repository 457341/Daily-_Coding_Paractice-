# ? Question
# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# ! Answer
def foo(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(foo([1,2,3]))
print(foo([1,1,3, 4, 5, 6, 7]))

