# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# formula for area of a circle: 2*PI*PI
import math
radius = float(input("Enter radius: "))

PI = math.pi
area = PI*radius ** 2
print("Area of a circle is: ",area)