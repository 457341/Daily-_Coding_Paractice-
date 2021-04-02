#  Write a Python program to sort three integers without using conditional statements and loops


def sort_interges(n1,n2,n3):
    arr = []
    arr.extend({n1,n2,n3})# All are same in order to add multiple values
    arr.extend((0,10,31)) # All are same in order to add multiple values
    arr.extend([15,20,7]) # All are same in order to add multiple values

    print(sorted(arr))
sort_interges(2,3,1)

# A different way
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)