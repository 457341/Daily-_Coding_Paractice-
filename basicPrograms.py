# Write a Python program to display your details like name, age, address in three different lines.
name = "Manzoor"
surname = "Hussain"

country = "Pakistan"
print("Name: {}\nSurname: {}\nCountry: {}".format(name,surname,country))


# the future value of a specified principal amount, rate of interest, and a number of years

# Formula:  FV = P(1 + rt).
def calculate_future_value(p,r,t):
    print("The future value is: ",p*(1 + r*t))

calculate_future_value(10000,3.5,7)
# est Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# Write a Python program to check whether a file exists.

import os
file = open('Notes.txt','r')
print(os.path.isfile('Notes.txt'))
print(os.path.isfile('exercise.txt'))