# Write a Python program to calculate the sum of a list of numbers.
def addition(lst):
    
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + addition(lst[1:])

lst = [1,2,3,4,5]
print(addition(lst))